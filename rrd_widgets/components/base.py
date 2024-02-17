"""
Qt-RoastedDuck-Widgets
======================
Qt widgets-based implementation of the Material Design specification.

Repository at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.

Demo are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/Demo.

Examples are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/examples.

Information:
    WeChat: Roast_71.
    csdnBlog: https://blog.csdn.net/m0_72760466?type=blog.

:copyright: (c) 2023 by Rev-RoastedDuck.
:license: GPLv3, see LICENSE for more details.
"""

from typing import Tuple, Any
from abc import abstractmethod
from PySide6.QtWidgets import QPushButton, QWidget, QLineEdit
from PySide6.QtCore import Property, QPropertyAnimation, Signal, QParallelAnimationGroup, QAbstractAnimation, \
    QEasingCurve


def animation_widget_decorator(cls:QWidget):
    class AnimationWidgetBase(cls):

        anim_param_change_signal = Signal(int)

        def __init__(self, parent=None):
            super().__init__(parent)
            self.anim_param = 0
            self.anim_msecs = 200

            self.anim = QPropertyAnimation(self, b'animParam', self)

        def __animInit(self) -> None:
            self.anim.setDuration(self.anim_msecs)
            # self.anim.setEasingCurve(QEasingCurve.OutQuad)
            self.anim_param_change_signal.connect(self.onAnimParamChangeSignal)

        def animForwardRun(self) -> None:
            self.anim.stop()
            self.min_anim_param, self.max_anim_param = self.get_anim_range()
            self.anim.setEndValue(self.max_anim_param)
            self.anim.start()

        def animBackwardRun(self) -> None:
            self.anim.stop()
            self.min_anim_param, self.max_anim_param = self.get_anim_range()
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
    return AnimationWidgetBase

def animation_group_widget_decorator(cls:QWidget):
    class QWidgetAnimationGroupBase(cls):
        anim_param_change_signal = Signal(list)

        def __init__(self, parent=None):
            super().__init__(parent)
            self.direction = QAbstractAnimation.Forward
            self.__animInit()

        def __animInit(self) -> None:
            self.anim_param_list: list = []
            self.anim_group: list[QAbstractAnimation] = []
            self.anim_param_change_signal.connect(self.onAnimParamChangeSignal)

        def addAnimParams(self, min_v: Any, max_v: Any, time: int) -> None:
            anim = QPropertyAnimation(self)
            anim.setDuration(time)
            anim.setStartValue(min_v)
            anim.setEndValue(max_v)
            anim.valueChanged.connect(self.__onValueChanged)

            self.anim_group.append(anim)

        def animForwardRun(self) -> None:
            self.stop()
            self.setDirection(QAbstractAnimation.Forward)
            self.start()

        def animBackwardRun(self) -> None:
            self.stop()
            self.setDirection(QAbstractAnimation.Backward)
            self.start()

        def is_running(self)->bool:
            for anim in self.anim_group:
                if anim.state() == QPropertyAnimation.Running:
                    return True
            return False

        def __onValueChanged(self, v: int) -> None:
            self.anim_param_list.append(v)
            if not len(self.anim_param_list) % (len(self.anim_group)):
                self.anim_param_change_signal.emit(self.anim_param_list)
                self.anim_param_list.clear()

        def stop(self):
            for anim in self.anim_group:
                anim.stop()

        def start(self):
            for anim in self.anim_group:
                anim.start()

        def setDirection(self,dir):
            for anim in self.anim_group:
                anim.setDirection(dir)
            self.direction = dir

        @abstractmethod
        def onAnimParamChangeSignal(self, v: list) -> None:
            """
            用于设置指定属性的值，把anim_param的值赋给指定的变量
            :param v: anima_param的数值
            :return:
            """
            pass
    return QWidgetAnimationGroupBase

@animation_widget_decorator
class ButtonAnimationBase(QPushButton):
    pass

@animation_widget_decorator
class WidgetAnimationBase(QWidget):
    pass

@animation_widget_decorator
class LineEditAnimationBase(QLineEdit):
    pass


@animation_group_widget_decorator
class WidgetAnimationGroupBase(QWidget):
    pass
