from PySide6.QtCore import Qt,Property, QPropertyAnimation, Signal
from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import  QPushButton

from typing import Tuple
from abc import  abstractmethod

class ButtonAnimationBase(QPushButton):

    anim_param_change_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.anim_param = 0

    def __animInit(self) -> None:
        self.anim = QPropertyAnimation(self, b'animParam', self)
        self.anim.setDuration(200)

        self.min_anim_param, self.max_anim_param = self.get_anim_range()
        self.anim_param = self.min_anim_param

        self.anim_param_change_signal.connect(self.onAnimParamChangeSignal)

    def animForwardRun(self) -> None:
        self.anim.stop()
        self.anim.setEndValue(self.max_anim_param)
        self.anim.start()

    def animBackwardRun(self) -> None:
        self.anim.stop()
        self.anim.setEndValue(self.min_anim_param)
        self.anim.start()

    @abstractmethod
    def get_anim_range(self) -> Tuple:
        pass

    @abstractmethod
    def onAnimParamChangeSignal(self, v) -> None:
        pass

    @Property(float)
    def animParam(self):
        return self.anim_param

    @animParam.setter
    def animParam(self, v):
        self.anim_param = v
        self.anim_param_change_signal.emit(v)
        self.update()

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self.__animInit()

class SimpleButtonBase(ButtonAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius:int = 0
        self.full_color:QColor = QColor()
        self.font_color:QColor = QColor()

    def setParams(self,
                  text: str,
                  full_color: QColor,
                  font_anim_start_color: QColor,
                  font_anim_finish_color: QColor,
                  border_radius: int = 5,
                  timer_interval: int = 10,
                  ):
        """
        :param text: showed text
        :param full_color: color used to fill button
        :param font_anim_start_color: font color when mouse is not hovering
        :param font_anim_finish_color:font color when mouse is hovering
        :param border_radius: border radius of button
        :param timer_interval:timer interval for each frame of animation
        :return:
        """
        self.setText(text)
        self.full_color = full_color
        self.border_radius = border_radius
        self.timer_interval = timer_interval
        self.font_anim_start_color = font_anim_start_color
        self.font_anim_finish_color = font_anim_finish_color

        self.font_color = self.font_anim_start_color

    def __drawText(self,painter:QPainter):
        """ 绘制文字 """
        painter.save()
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text():
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.restore()

    def __drawBorder(self,painter:QPainter):
        painter.save()
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(self.full_color)

        painter.setPen(pen)
        painter.drawRoundedRect(self.rect(),self.border_radius,self.border_radius)
        painter.restore()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        self.__drawBorder(painter)
        self.drawForeground(painter)
        self.__drawText(painter)

    def drawForeground(self, painter: QPainter):
        pass