from PySide6.QtCore import QRect, Qt, QTimer, QRectF
from PySide6.QtWidgets import QApplication, QPushButton,QWidget
from PySide6.QtGui import QBrush, QColor, QFont, QPainter, QPainterPath

from Tool.getStyleProperty import get_property, transfer_type

class SimpleButton_4(QPushButton):
    def __init__(self,parent=None):
        super(SimpleButton_4, self).__init__(parent)
        self.text = ""

    def setParams(self,
                  full_color: QColor = None,
                  font_anim_finish_color:QColor = None,
                  timer_interval: int = None,
                  ):
        """
        :param full_color: 填充颜色
        :param font_anim_finish_color: 变化后的按钮字体颜色
        :param timer_interval: 微光流动时间间隔，数值越小，变化速度越快
        """
        self.full_color = full_color
        self.timer_interval = timer_interval
        self.font_anim_finish_color = font_anim_finish_color


    def getStyleSheetParams(self):
        """ 提取样式 """
        SimpleButton_4_property: dict = get_property(self)["SimpleButton_4"]
        self.border_radius = transfer_type(SimpleButton_4_property["border-radius"], "pixel")
        self.font_color_origin = transfer_type(SimpleButton_4_property["color"], "color")
        self.font_color = self.font_color_origin

    def animationConfig(self):
        self.rect_width_var = 5             # 宽度变化值
        self.rect_width = 0                 # 起始宽度
        self.rect_max_width = self.width()  # 最大宽度

        self.timer = QTimer(self)
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(self.incWidth)

        self.is_enter = False

    def incWidth(self):
        self.rect_width += self.rect_width_var
        if self.rect_width > self.rect_max_width:
            self.timer.stop()
            return
        self.update()

    def decWidth(self):
        self.rect_width -= self.rect_width_var
        if self.rect_width < 0:
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
        super(SimpleButton_4, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        brush = QBrush(self.full_color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        if self.is_enter:
            painter.drawRect(QRectF(0, 0, self.rect_width, self.height()))
        elif not self.is_enter:
            # 从右到左绘画矩形
            painter.translate(self.width(), self.height())
            painter.rotate(180)
            painter.drawRect(QRectF(0, 0, self.rect_width, self.height()))

        self.paintText()

    def enterEvent(self, event):
        self.is_enter = True
        self.font_color = self.font_anim_finish_color
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incWidth)
        self.timer.start()

    def leaveEvent(self, event):
        self.is_enter = False
        self.font_color = self.font_color_origin
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decWidth)
        self.timer.start()

    def showEvent(self, event) -> None:
        super(SimpleButton_4, self).showEvent(event)
        self.animationConfig()

    def setStyleSheet(self, styleSheet: str) -> None:
        super(SimpleButton_4, self).setStyleSheet(styleSheet)
        self.getStyleSheetParams()

