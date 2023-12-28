import sys
from typing import Any
from PySide6.QtCore import (QSize, Qt, QAbstractAnimation, QPropertyAnimation, Signal,
                            QParallelAnimationGroup)
from PySide6.QtGui import (QColor, QFont,QIcon, QPainter, QPainterPath)
from PySide6.QtWidgets import (QApplication, QPushButton, QVBoxLayout,QWidget)
from abc import abstractmethod
import icon


class QWidgetAnimationGroupBase(QWidget):
    """
        触发条件:鼠标划入滑出
    """

    anim_param_change_signal = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__animInit()

    def __animInit(self) -> None:
        self.anim_param_count = 0
        self.anim_param_list: list = []
        self.anim_group = QParallelAnimationGroup()
        self.anim_param_change_signal.connect(self.onAnimParamChangeSignal)

    def addAnimParams(self, min_v: Any, max_v: Any, time: int) -> None:
        anim = QPropertyAnimation(self)
        anim.setDuration(time)
        anim.setStartValue(min_v)
        anim.setEndValue(max_v)
        anim.valueChanged.connect(self.__onValueChanged)

        self.anim_param_count += 1
        self.anim_group.addAnimation(anim)

    def animForwardRun(self) -> None:
        self.anim_group.stop()
        self.anim_group.setDirection(QAbstractAnimation.Forward)
        self.anim_group.start()

    def animBackwardRun(self) -> None:
        self.anim_group.stop()
        self.anim_group.setDirection(QAbstractAnimation.Backward)
        self.anim_group.start()

    def __onValueChanged(self, v: int) -> None:
        """
        每次动画属性值变化，都会把值存在列表内，每一次循环插值，都会返回一个列表
        :param v:
        :return:
        """
        self.anim_param_list.append(v)
        if not len(self.anim_param_list) % (self.anim_param_count):
            self.anim_param_change_signal.emit(self.anim_param_list)
            self.anim_param_list.clear()

    @abstractmethod
    def onAnimParamChangeSignal(self, v: list) -> None:
        """
        用于设置指定属性的值，吧anim_param的值赋给指定的变量
        :param v: anima_param的数值
        :return:
        """
        pass


class FlexibleSidebarButton(QPushButton):
    def __init__(self, parent, text=None, icon=None):
        super().__init__(parent=parent, text=text, icon=icon)
        self.need_show_text = True
        self.border_radius = 0
        self.font_color = QColor()
        self.background_color = QColor()

        self.setFixedHeight(30)
        self.text_backpack = text

    def hideText(self) -> None:
        self.need_show_text = False

    def showText(self) -> None:
        self.need_show_text = True

    def setParams(self,
                  font_color: QColor,
                  background_color: QColor,
                  border_radius: int = 5,
                  ):
        self.font_color = font_color
        self.border_radius = border_radius
        self.background_color = background_color

    def setText(self, text: str) -> None:
        super().setText(text)
        self.text_backpack = text

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        self.drawForeground(painter)
        self.drawIcon(painter)
        self.drawText(painter)

    def drawIcon(self, painter: QPainter):
        painter.save()
        if self.icon():
            pixmap = self.icon().pixmap(self.height()*0.7)
            # pixmap = pixmap.scaled(int(pixmap.width() * 0.8), int(pixmap.height() * 0.8))
            painter.drawPixmap(4, 4, pixmap)
        painter.restore()

    def drawText(self, painter: QPainter):
        painter.save()
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text() and self.need_show_text:
            painter.drawText(self.rect().adjusted(35, 0, 0, 0), Qt.AlignLeft | Qt.AlignVCenter, self.text())
        painter.restore()

    def drawForeground(self, painter: QPainter):
        painter.save()
        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())
        painter.restore()


class FlexibleSidebar(QWidgetAnimationGroupBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.min_v = 0
        self.max_v = 0
        self.border_radius = 0
        self.background_color = QColor()

        self.enterFlag = False
        self.setMaximumWidth(300)

        self.componentInit()

    def setParams(self,
                  min_of_range:int,
                  max_of_range:int,
                  background_color: QColor,
                  border_radius: int = 0,
                  ):
        self.min_v = min_of_range
        self.max_v = max_of_range
        self.border_radius = border_radius
        self.background_color = background_color


    def componentInit(self):
        self.vbox = QVBoxLayout(self)
        self.vbox.addStretch()
        self.vbox.setSpacing(8)
        self.vbox.setContentsMargins(10, 10, 10, 10)

    def animConfig(self):
        self.start_show_x = self.x()
        self.start_hide_x = self.x() + (self.max_v - self.min_v) // 2
        self.addAnimParams(min_v=self.min_v, max_v=self.max_v, time=150)
        self.addAnimParams(min_v=self.start_hide_x, max_v=self.start_show_x, time=150)

    def paintEvent(self, event) -> None:
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)

        self.drawForeground(painter)

    def drawForeground(self, painter: QPainter):
        painter.save()
        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())
        painter.restore()

    def addWidget(self, widget: QWidget):
        self.vbox.insertWidget(0, widget)


    def onAnimParamChangeSignal(self, v: list) -> None:
        x = v[1]
        width = v[0]
        self.setGeometry(x, self.y(), width, self.height())

    def enterEvent(self, event):
        if not self.enterFlag:
            self.enterFlag = True
            return
        super().enterEvent(event)
        for item in self.findChildren(FlexibleSidebarButton):
            if isinstance(item, FlexibleSidebarButton):
                item.showText()
        self.is_focus = True
        self.animForwardRun()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        for item in self.findChildren(FlexibleSidebarButton):
            if isinstance(item, FlexibleSidebarButton):
                item.hideText()
        self.is_focus = False
        self.animBackwardRun()

    def showEvent(self, event) -> None:
        super(FlexibleSidebar, self).showEvent(event)
        self.animConfig()


