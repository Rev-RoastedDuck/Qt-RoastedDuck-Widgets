from PySide6.QtCore import QRect, QSize, Qt, QTimer, QRegularExpression, QPoint, Property, QPropertyAnimation, Signal, \
    QRectF, QParallelAnimationGroup, QAbstractAnimation
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QPainter, QPainterPath, QIcon, QPen
from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QWidget

from typing import Union, TypedDict, Tuple, Any
from abc import ABC, abstractmethod

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


class RWavyButtonBase(ButtonAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius:int = 0
        self.full_color:QColor = QColor()
        self.font_color:QColor = QColor()

    def setParams(self,*args):
        pass

    def drawText(self,painter:QPainter):
        painter.save()
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text():
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.restore()

    def drawBorder(self,painter:QPainter):
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

        self.drawBorder(painter)
        self.drawForeground(painter)
        self.drawText(painter)

    def drawForeground(self, painter: QPainter):
        pass
