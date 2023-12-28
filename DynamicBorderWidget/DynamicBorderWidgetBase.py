from abc import abstractmethod
from typing import Tuple

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QPropertyAnimation, Property


class WidgetAnimationBase(QWidget):
    """
        触发条件:鼠标划入滑出
    """

    anim_param_change_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.anim_param = 0
        self.anim_msecs = 200
        self.is_infinite = False

    def __animInit(self) -> None:
        self.anim = QPropertyAnimation(self, b'animParam', self)
        self.anim.setDuration(self.anim_msecs)

        self.min_anim_param, self.max_anim_param = self.get_anim_range()
        self.anim_param = self.min_anim_param

        self.anim_param_change_signal.connect(self.onAnimParamChangeSignal)

        if self.is_infinite:
            self.anim.setLoopCount(-1)

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
        """
        获得动画差值的范围
        :return:
        """
        pass

    @abstractmethod
    def onAnimParamChangeSignal(self, v) -> None:
        """
        用于设置指定属性的值，吧anim_param的值赋给指定的变量
        :param v: anima_param的数值
        :return:
        """
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