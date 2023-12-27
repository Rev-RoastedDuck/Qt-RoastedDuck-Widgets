from PySide6.QtCore import Property, QPropertyAnimation, Signal
from PySide6.QtWidgets import  QPushButton

from typing import Tuple
from abc import abstractmethod

class ButtonAnimationBase(QPushButton):

    anim_param_change_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.anim_param = 0

    def __animInit(self) -> None:
        self.anim = QPropertyAnimation(self, b'animParam', self)
        self.anim.setDuration(1000)

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

