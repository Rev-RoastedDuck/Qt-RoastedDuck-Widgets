from PySide6.QtCore import QRect, QSize, Qt, QTimer, QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint, \
    QSequentialAnimationGroup, QAbstractAnimation, QRegularExpression
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QPainter, QPainterPath, QLinearGradient
from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QWidget, QLineEdit, QGraphicsBlurEffect


class RPushButton(QFrame):
    def __init__(self, parent=None):
        super(RPushButton, self).__init__(parent)

    def ui(self):
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(self.setBorder())

        font = QFont()
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setText("Start Coding")


    def setStyleSheetConfig(self):
        '''
        正则提取样式
        :return:
        '''
        radius_match = QRegularExpression(r"border-radius:(?P<border_radius>\d+)px;")
        radius_result = radius_match.match(self.styleSheet())
        if radius_result.hasMatch():
            self.border_radius  = int(radius_result.captured("border_radius"))

        Rborder_width_match = QRegularExpression(r"Rborder-width:(?P<Rborder_width>\d+)px;")
        Rborder_width_result = Rborder_width_match.match(self.styleSheet())
        if Rborder_width_result.hasMatch():
            self.border  = int(Rborder_width_result.captured("Rborder_width"))

        self.ui()
        self.animationConfig()

    def animationConfig(self):
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.offsetUpdate)

        self.rect_1_offset = 0            # 矩形1的坐标
        self.rect_2_offset = 0            # 矩形2的坐标
        self.rect_1_start = 0             # 矩形1初始位置
        self.rect_2_start = -self.width() # 矩形2初始位置
        self.init_x = -self.width()       # 默认初始位置
        self.flag = 0                     # 矩形1的初始位置标志，0 -> 矩形1在矩形1初始位置  1 -> 矩形1在默认初始位置

    def setBorder(self):
        '''
        根据边框宽度，设置内部按钮位置及大小
        :return:
        '''
        btn_width = self.width() - self.border * 2
        btn_height = self.height() - self.border * 2
        btn_x = self.border
        btn_y = self.border
        return QRect(btn_x,btn_y,btn_width,btn_height)

    def paintEvent(self, event):
        '''
        绘制颜色
        :param event:
        :return:
        '''
        super(RPushButton, self).paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)

        gradient_1 = self.createGradient(self.rect_1_start + self.rect_1_offset)
        painter.setBrush(gradient_1)
        painter.drawRect(self.rect_1_start + self.rect_1_offset, 0, self.width(), self.height())

        gradient_2 = self.createGradient(self.rect_2_start + self.rect_2_offset)
        painter.setBrush(gradient_2)
        painter.drawRect(self.rect_2_start + self.rect_2_offset, 0, self.width(), self.height())



    def createGradient(self, x):
        '''
        设置渐变颜色
        :param x: 矩形的横坐标
        :return:
        '''
        gradient = QLinearGradient(x, 0, x+self.width(), 0)
        gradient.setColorAt(0, QColor(0, 164, 128, 230))
        gradient.setColorAt(0.166, QColor(13, 88, 166, 230))
        gradient.setColorAt(0.333, QColor(118, 8, 170, 230))
        gradient.setColorAt(0.5, QColor(255, 144, 0, 230))
        gradient.setColorAt(0.666, QColor(255, 255, 0, 230))
        gradient.setColorAt(0.833, QColor(165, 239, 0, 230))
        gradient.setColorAt(1, QColor(83, 223, 0, 230))
        return gradient

    def enterEvent(self, event):
        self.timer.start()

    def leaveEvent(self, event):
        self.timer.stop()

    def offsetUpdate(self):
        '''
        判断矩形是否离开按钮，并触发更新事件
        :return:
        '''
        if self.rect_1_offset >= self.width() and not self.flag:
            self.rect_1_offset = 0
            self.rect_1_start = self.init_x
            self.flag = 1

        # if self.rect_1_offset >= self.width() * 2 and self.flag:
        #     self.rect_1_offset = 0
        #     self.rect_1_start = self.init_x

        if self.rect_2_offset >= self.width() * 2:
            self.rect_2_offset = 0
            self.rect_2_start = self.init_x

        self.rect_1_offset += 3
        self.rect_2_offset += 3

        self.update()


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background-color:#000000")

    a = RPushButton(w)
    a.setGeometry(QRect(290, 280, 300, 100))
    a.setStyleSheet(u"QFrame{"
                       "	background-color: rgba(255, 255, 255,0);"
                       "}"
                       "*{"
                       "	border:none;"
                       "	border-radius:10px;"
                       "  Rborder-width:5px;"
                       ""
                       "}"
                       "QPushButton{color:#ffffff;}"
                       )

    a.setStyleSheetConfig()


    w.show()
    app.exec()
