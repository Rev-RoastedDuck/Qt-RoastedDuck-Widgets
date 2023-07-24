from PySide6.QtCore import QRect,QSize,Qt, QTimer
from PySide6.QtGui import QBrush, QColor,QCursor,QFont,  QPainter,QPainterPath
from PySide6.QtWidgets import QApplication, QFrame, QPushButton,QWidget


class MyPushButton(QFrame):
    def __init__(self, parent=None, geometry:QRect=None, minSize:QSize=None):
        super(MyPushButton, self).__init__(parent)
        self.geometry = geometry
        self.minSize = minSize
        self.ui()
        self.animationConfig()

    def ui(self):
        self.setMinimumSize(self.minSize)
        self.setStyleSheet(u"QFrame{"
                                 "	background-color: rgb(46, 22, 177);"
                                 "}"
                                 "*{"
                                 "	border:none;"
                                 "	border-radius:10px"
                                 ""
                                 "}"
                                 "QPushButton{"
                                 "	background-color: rgba(255, 255, 255, 0);"
                                 "	color: rgb(255, 255, 255);"
                                 "}")

        self.pushButton = QPushButton(self)
        self.pushButton.setMinimumSize(self.minSize)
        self.pushButton.setFixedSize(QSize(self.width(),self.height()))
        font = QFont()
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setText("悬浮会变色喔")

        self.setGeometry(self.geometry)

    def animationConfig(self):
        self.corner_radius = 10                                    # 按钮的圆角半径
        self.radiusVar = 2                                         # 半径变化值
        self.radius = 0                                            # 起始半径
        self.max_radius = (self.width()**2+self.height()**2)**0.5  # 最大半径
        self.center = None                                         # 鼠标点击坐标
        self.color = QColor(255, 89, 0)                            # 填充颜色
        self.msec = 10                                             # 定时时间

        self.timer = QTimer(self)
        self.timer.setInterval(self.msec)
        self.timer.timeout.connect(self.incRadius)

    def incRadius(self):
        self.radius += self.radiusVar
        if self.radius > self.max_radius:
            self.timer.stop()
            return
        self.update()

    def decRadius(self):
        self.radius -= self.radiusVar
        if self.radius < 0:
            self.timer.stop()
            return

        self.update()

    def paintEvent(self, event):
        super(MyPushButton, self).paintEvent(event)
        if self.center is None:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(self.color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.corner_radius, self.corner_radius)
        painter.setClipPath(path)

        painter.drawEllipse(self.center, self.radius, self.radius)

    def enterEvent(self, event):
        self.center = event.position()
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incRadius)
        self.timer.start()

    def leaveEvent(self, event):
        self.center = self.mapFromGlobal(QCursor.pos())
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decRadius)
        self.timer.start()


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00bd39, "
                         "stop:0.1 #00b844, stop:0.2 #00b44f, stop:0.3 #00af59, stop:0.4 #00aa64, "
                         "stop:0.5 #01a66f, stop:0.6 #01a17a, stop:0.7 #019c84, stop:0.8 #01988f, "
                         "stop:0.9 #01939a);")
    a = MyPushButton(w,QRect(290, 280, 440, 140),QSize(440, 140))
    w.show()
    app.exec()
