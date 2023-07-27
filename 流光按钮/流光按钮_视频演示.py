from PySide6.QtCore import QRect, QSize, Qt, QTimer, QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint, \
    QSequentialAnimationGroup, QAbstractAnimation, QRegularExpression
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QPainter, QPainterPath, QLinearGradient
from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QWidget, QLineEdit, QGraphicsBlurEffect


class RPushbutton(QFrame):
    def __init__(self,parent = None):
        super(RPushbutton, self).__init__(parent)
        self.ui()
        self.animationConfig()

    def ui(self):
        self.setGeometry(QRect(290,280,300,100))
        self.setStyleSheet("QFrame{backgound-color:rgba(255,255,255,0);}"
                           "*{border:none;border-radius:10px;Rborder-width:5px;}"
                           "QPushButton{color:rgba(255,255,255,255)}")

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(5,5,300 - 5 * 2,100 - 5 * 2)

        font = QFont()
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setText("Start Coding")

    def animationConfig(self):
        self.rect_1_offset = 0 # 矩形1的位置
        self.rect_2_offset = 0 # 矩形2的位置
        self.rect_1_start = 0  # 矩形1的起始位置
        self.rect_2_start = -self.width()  # 矩形2的起始位置
        self.init_x = -self.width() # 第一次循环过后，两个矩形的初始位置
        self.flag = 0 # 判断矩形1是否进入第二次循环

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)

    def paintEvent(self,event):
        super(RPushbutton, self).paintEvent(event)

        # 绘画路径
        path = QPainterPath()
        path.addRoundedRect(0,0,self.width(),self.height(),10,10)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)

        # 设置渐变颜色
        gradient_1 = QLinearGradient(self.rect_1_start + self.rect_1_offset,0,self.rect_1_start + self.rect_1_offset+self.width(),0)
        gradient_1.setColorAt(0, QColor(0, 164, 128, 230))
        gradient_1.setColorAt(0.166, QColor(13, 88, 166, 230))
        gradient_1.setColorAt(0.333, QColor(118, 8, 170, 230))
        gradient_1.setColorAt(0.5, QColor(255, 144, 0, 230))
        gradient_1.setColorAt(0.666, QColor(255, 255, 0, 230))
        gradient_1.setColorAt(0.833, QColor(165, 239, 0, 230))
        gradient_1.setColorAt(1, QColor(83, 223, 0, 230))
        painter.setBrush(gradient_1)
        painter.drawRect(self.rect_1_start + self.rect_1_offset,0,self.width(),self.height())

        # 设置矩形2的渐变颜色
        gradient_2 = QLinearGradient(self.rect_2_start + self.rect_2_offset,0,self.rect_2_start + self.rect_2_offset+self.width(),0)
        gradient_2.setColorAt(0, QColor(0, 164, 128, 230))
        gradient_2.setColorAt(0.166, QColor(13, 88, 166, 230))
        gradient_2.setColorAt(0.333, QColor(118, 8, 170, 230))
        gradient_2.setColorAt(0.5, QColor(255, 144, 0, 230))
        gradient_2.setColorAt(0.666, QColor(255, 255, 0, 230))
        gradient_2.setColorAt(0.833, QColor(165, 239, 0, 230))
        gradient_2.setColorAt(1, QColor(83, 223, 0, 230))
        painter.setBrush(gradient_2)
        painter.drawRect(self.rect_2_start + self.rect_2_offset,0,self.width(),self.height())

        # 判断矩形是否离开显示区域
        if self.rect_1_offset >= self.width() and not self.flag:
            self.rect_1_offset = 0
            self.rect_1_start = self.init_x
            self.flag = 1

        if self.rect_1_offset >= self.width() * 2 and self.flag:
            self.rect_1_offset = 0
            self.rect_1_start = self.init_x

        if self.rect_2_offset >= self.width() * 2:
            self.rect_2_offset = 0
            self.rect_2_start = self.init_x

        self.rect_1_offset += 3
        self.rect_2_offset += 3

    def enterEvent(self,event):
        super(RPushbutton, self).enterEvent(event)
        self.timer.start()



if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background-color:#000000")
    btn = RPushbutton(w)

    w.show()
    app.exec()