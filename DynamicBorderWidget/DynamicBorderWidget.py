from typing import Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QColor, QConicalGradient, QPainterPath, QFont, QPixmap

from DynamicBorderWidgetBase import WidgetAnimationBase


class DynamicBorderWidget(WidgetAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_infinite = True
        self.anim_msecs = 8000
        self.componentInit()

    def componentInit(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

    def get_anim_range(self) -> Tuple:
        min_v = 0
        max_v = 360
        return min_v,max_v

    def onAnimParamChangeSignal(self, v) -> None:
        self.angle = v

    def setParams(self,
                  border_width:int,
                  border_radius:int,
                  color_1: QColor,
                  color_2: QColor,
                  font_color: QColor,
                  inside_background_color:QColor,
                  ):
        self.color_1 = color_1
        self.color_2 = color_2
        self.font_color = font_color
        self.inside_background_color = inside_background_color

        self.border_width = border_width
        self.border_radius = border_radius

        self.label.setGeometry(self.border_width, self.border_width, self.width() - self.border_width * 2, self.height() - self.border_width * 2)
        self.label.setStyleSheet(f"""QLabel{{
                                    color: {self.font_color.name()};
                                    background-color: {self.inside_background_color.name()};
                                    border-radius:{self.border_radius - 5}px;
                                    }}
                                  """
                                 )

    def paintEvent(self, event):
        super(DynamicBorderWidget, self).paintEvent(event)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)

        self.drawForeground(painter)


    def drawForeground(self, painter: QPainter):
        painter.save()
        gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0)  # 设置锥形渐变原点为卡片中心
        gradient.setColorAt(0, QColor(0, 0, 0, 255))
        gradient.setColorAt(0.5, self.color_1)
        painter.setBrush(gradient)
        painter.rotate(self.angle)  # 旋转画笔
        painter.drawRect(0, 0, self.width(), self.height())

        painter.restore()

        # 绘制第二条边框
        gradient.setColorAt(0, QColor(0, 0, 0, 255))
        gradient.setColorAt(0.5, self.color_2)
        painter.setBrush(gradient)
        painter.rotate(self.angle + 180)
        painter.drawRect(0, 0, self.width(), self.height())

        painter.restore()

    def showEvent(self, event):
        super().showEvent(event)
        self.animForwardRun()

    def setFont(self, font: QFont):
        self.label.setFont(font)

    def setText(self,text:str):
        self.label.setText(text)

    def setPixmap(self,pximap:QPixmap):
        self.label.setPixmap(pximap)



