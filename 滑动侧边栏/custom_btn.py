
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Property, QAbstractAnimation, QPropertyAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QPainterPath)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
                               QSizePolicy, QWidget, QLabel)
import icon
class MyFrame(QFrame):
    def __init__(self,parent,text=None,icon=None):
        super(MyFrame, self).__init__(parent)
        self._color_1 = QColor(255, 116, 0,255)
        self.parent = parent
        self.iconFile = icon
        self.setText = text
        self.ui()

    def ui(self):
        self.resize(110,30)
        self.setMinimumSize(40,30)
        self.setMaximumSize(110, 30)
        self.setStyleSheet(u"QFrame{\n"
                                   "	border-radius: 10px;\n"
                                   "	background-color: rgba(255, 116, 0,255);\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "QPushButton{\n"
                                   "	border-radius: 10px;\n"
                                   "	background-color: rgba(255, 116, 0,255);\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "}")
        self.pushButton_icon = QPushButton(self)
        self.pushButton_icon.setObjectName(u"pushButton_icon")
        self.pushButton_icon.setGeometry(QRect(0, 0, 30, 31))
        self.pushButton_icon.setStyleSheet(u"padding-left:10px")
        icon = QIcon()
        icon.addFile(self.iconFile, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_icon.setIcon(icon)
        self.pushButton_icon.setIconSize(QSize(20, 20))

        self.pushButton_btn = QPushButton(self)
        self.pushButton_btn.setObjectName(u"pushButton_btn")
        self.pushButton_btn.setGeometry(QRect(30, 0, 80, 31))
        self.pushButton_btn.setStyleSheet(u"padding-left:15px;\n"
                                         "text-align: left;")
        self.pushButton_btn.setIconSize(QSize(20, 20))
        self.pushButton_btn.setText(self.setText)
        self.pushButton_btn.setCheckable(True)

        self.animation = QPropertyAnimation()

    @Property(QColor)
    def color_1(self):
        return self._color_1

    @color_1.setter
    def color_1(self,color):
        self._color_1 = color
        self.updateColor_1()

    def updateColor_1(self):
        self.setStyleSheet(f"QFrame{{border-radius: 10px;background-color: rgba(255, 116, 200,225);}}QPushButton{{border-radius: 10px;background-color: rgba(255, 116, 0,0);color: rgb(255, 255, 255);}}")

    def paintEvent(self,event):
        super(MyFrame, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        painter.setPen(Qt.NoPen)

        # 绘制圆角矩形背景
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        painter.fillPath(path, self._color_1)



    def lableAnimation(self):
        self.animation.setTargetObject(self)
        self.animation.setPropertyName(b"color_1")
        self.animation.setDuration(300)
        self.animation.setStartValue(QColor(255, 116, 0,255))
        self.animation.setEndValue(QColor(255, 116, 200,225))
        self.animation.start()

    def enterEvent(self,event):
        self.animation.setDirection(QAbstractAnimation.Forward)
        self.lableAnimation()
        super(MyFrame, self).enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Backward)
        self.lableAnimation()