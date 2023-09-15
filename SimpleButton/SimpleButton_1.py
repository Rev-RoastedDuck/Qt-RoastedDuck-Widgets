from PySide6.QtCore import QRect, Qt, QTimer, QPoint
from PySide6.QtWidgets import QApplication, QPushButton,QWidget
from PySide6.QtGui import QBrush, QColor, QFont, QPainter, QPainterPath

from Tool.getStyleProperty import get_property, transfer_type


class SimpleButton_1(QPushButton):
    def __init__(self,parent=None):
        super(SimpleButton_1, self).__init__(parent)
        self.text = ""

    def setParams(self,
                  full_color: QColor = None,
                  font_anim_finish_color:QColor = None,
                  timer_interval: int = None,
                  ):
        """
        :param full_color: 填充颜色
        :param font_anim_finish_color: 变化后的按钮字体颜色
        :param timer_interval: 动画更新间隔
        """
        self.full_color = full_color
        self.timer_interval = timer_interval
        self.font_anim_finish_color = font_anim_finish_color


    def getStyleSheetParams(self):
        """ 提取样式 """
        SimpleButton_1_property: dict = get_property(self)["SimpleButton_1"]
        self.border_radius = transfer_type(SimpleButton_1_property["border-radius"], "pixel")
        self.font_color_origin = transfer_type(SimpleButton_1_property["color"], "color")
        self.font_color = self.font_color_origin

    def animationConfig(self):
        self.radiusVar = 3                                         # 半径变化值
        self.radius = 0                                            # 起始半径
        self.max_radius = (self.width()**2+self.height()**2)**0.5  # 最大半径


        self.timer = QTimer(self)
        self.timer.setInterval(self.timer_interval)
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

    def setText(self, text):
        self.text = text

    def paintText(self):
        """ 绘制文字 """
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))
        painter.setRenderHint(QPainter.Antialiasing)

        if self.text:
            painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def paintEvent(self, event):
        super(SimpleButton_1, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(self.full_color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        painter.drawEllipse(QPoint(0,0), self.radius, self.radius)
        painter.drawEllipse(QPoint(self.width(),self.height()), self.radius, self.radius)

        self.paintText()

    def enterEvent(self, event):
        self.font_color = self.font_anim_finish_color
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incRadius)
        self.timer.start()

    def leaveEvent(self, event):
        self.font_color = self.font_color_origin
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decRadius)
        self.timer.start()

    def showEvent(self, event) -> None:
        super(SimpleButton_1, self).showEvent(event)
        self.animationConfig()

    def setStyleSheet(self, styleSheet: str) -> None:
        super(SimpleButton_1, self).setStyleSheet(styleSheet)
        self.getStyleSheetParams()