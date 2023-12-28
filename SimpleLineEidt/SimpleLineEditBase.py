from abc import abstractmethod
from typing import Tuple

from PySide6.QtCore import Qt, QPropertyAnimation, Signal, Property
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QColor, QPainter, QPainterPath


class LineEditAnimationBase(QLineEdit):
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


class LineEditBase(LineEditAnimationBase):
    def __init__(self, parent=None):
        super(LineEditBase, self).__init__(parent)
        self.border_radius: int = 0

        self.setFocusPolicy(Qt.ClickFocus)
        self.setProperty("transparent", True)

    @abstractmethod
    def setParams(self, font_color:QColor,*args):
        self.setStyleSheet(f"LineEditBase{{color:'{font_color.name()}';border:none;padding-left:10px;}}")
        pass

    def paintEvent(self, event):
        super().paintEvent(event)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawForeground(painter)

    def drawForeground(self, painter):
        pass

