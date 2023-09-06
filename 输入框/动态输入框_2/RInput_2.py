import sys

from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtWidgets import QApplication,QWidget,QLineEdit
from PySide6.QtGui import  QColor,QFont, QPainter, QPainterPath, QPen



class RInput_2_1(QLineEdit):
    def __init__(self, parent=None):
        super(RInput_2_1, self).__init__(parent)
        self.border_radius = 10
        self.line_height = 2
        self.line_width_anim = 0
        self.line_width_offset = 10
        self.line_is_show = False

        self.setFocusPolicy(Qt.ClickFocus)

        self.animParamsConfig()

    def animParamsConfig(self):
        self.msec = 10
        self.timer = QTimer(self)
        self.timer.setInterval(self.msec)
        self.timer.timeout.connect(self.incWidthOfLine)

    def incWidthOfLine(self):
        self.line_width_anim += self.line_width_offset
        if self.line_width_anim > self.width():
            self.timer.stop()
        self.update()

    def decWidthOfLine(self):
        self.line_width_anim -= self.line_width_offset
        if self.line_width_anim < 0:
            self.timer.stop()
        self.update()

    def paintEvent(self, event):
        super(RInput_2_1, self).paintEvent(event)

        self.line_color_1 = "#444444"
        self.line_color = "#007bff"

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor(self.line_color_1), self.line_height, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, self.height() - self.line_height),QPointF(self.width(), self.height() - self.line_height))

        pen = QPen(QColor(self.line_color), self.line_height, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, self.height() - self.line_height), QPointF(self.line_width_anim, self.height() - self.line_height))

        painter.end()

    def focusInEvent(self, event):
        super(RInput_2_1, self).focusInEvent(event)
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incWidthOfLine)
        self.timer.start()

    def focusOutEvent(self, event):
        super(RInput_2_1, self).focusOutEvent(event)
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decWidthOfLine)
        self.timer.start()

class RInput_2_2(QLineEdit):
    def __init__(self, parent=None):
        super(RInput_2_2, self).__init__(parent)
        self.setFocusPolicy(Qt.ClickFocus)
        self.border_radius = 0
        self.line_width = 2


    def paintEvent(self, event):
        super(RInput_2_2, self).paintEvent(event)
        if not self.hasFocus():
            self.line_color = "#444444"
        else:
            self.line_color = "#007bff"

        path = QPainterPath()
        path.addRoundedRect(0, -20, self.width(), self.height()+20, self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor(self.line_color), self.line_width, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(0,self.height()-self.line_width+1),QPointF(self.width(),self.height()-self.line_width+1))

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1900,800)
    w.setStyleSheet("background-color:#000000")

    font = QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(10)

    a = RInput_2_2(w)
    a.setStyleSheet("RInput_2_2{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a.setGeometry(600,300,200,35)
    a.setPlaceholderText("请输入文字")
    a.setFont(font)

    a_1 = RInput_2_2(w)
    a_1.setStyleSheet("RInput_2_2{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_1.setGeometry(600,340,200,35)
    a_1.setPlaceholderText("请输入文字")
    a_1.setFont(font)

    a_2 = RInput_2_1(w)
    a_2.setStyleSheet("RInput_2_1{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_2.setGeometry(600,380,200,35)
    a_2.setPlaceholderText("请输入文字")
    a_2.setFont(font)

    a_3 = RInput_2_1(w)
    a_3.setStyleSheet("RInput_2_1{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_3.setGeometry(600,420,200,35)
    a_3.setPlaceholderText("请输入文字")
    a_3.setFont(font)



    w.show()
    app.exec()


