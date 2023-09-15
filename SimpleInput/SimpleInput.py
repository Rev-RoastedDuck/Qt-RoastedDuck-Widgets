import sys

from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtWidgets import QApplication,QWidget,QLineEdit
from PySide6.QtGui import  QColor,QFont, QPainter, QPainterPath, QPen



class SimpleInput_1(QLineEdit):
    def __init__(self, parent=None):
        super(SimpleInput_1, self).__init__(parent)
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
        super(SimpleInput_1, self).paintEvent(event)

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
        super(SimpleInput_1, self).focusInEvent(event)
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incWidthOfLine)
        self.timer.start()

    def focusOutEvent(self, event):
        super(SimpleInput_1, self).focusOutEvent(event)
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decWidthOfLine)
        self.timer.start()

class SimpleInput_2(QLineEdit):
    def __init__(self, parent=None):
        super(SimpleInput_2, self).__init__(parent)
        self.setFocusPolicy(Qt.ClickFocus)
        self.border_radius = 0
        self.line_width = 2


    def paintEvent(self, event):
        super(SimpleInput_2, self).paintEvent(event)
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



