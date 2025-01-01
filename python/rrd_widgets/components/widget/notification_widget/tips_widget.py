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

from enum import Enum
from typing import TypedDict, Tuple

from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor,QFont, QPainter,QPainterPath, QPen, QTextOption
from PySide6.QtCore import Qt, QSize, QRect,QPropertyAnimation, QEasingCurve, QAbstractAnimation,QPoint, QTimer

from rrd_widgets.components.base import WidgetAnimationBase
from ....common.icon.rendered_icon.rendered_icon import drawHook,drawFork,drawInvalidation,drawExclamation


class TipsStatus(Enum):
    Succeed = 1
    Warning = 2
    Dangerous = 3


class ColorConfig(TypedDict):
    top_color: QColor
    hook_color: QColor
    fork_color: QColor
    text_color: QColor
    below_color: QColor
    background_color: QColor

class TipsWidget(WidgetAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.message = ""
        self.__status = TipsStatus.Warning

        self.__uiInit()
        self.anim_y = 0
        self.anim_msecs = 2000

    def __uiInit(self):
        self.max_height = 35
        self.border_radius = 5
        self.setFixedWidth(420)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(2, 2)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(20, 20, 20, 30))
        self.setGraphicsEffect(shadow)

    def __fin(self):
        self.anim_show.setDirection(QAbstractAnimation.Backward)
        self.anim_show.start()
        self.anim_show.finished.connect(self.__delWidget)

    def __delWidget(self):
        self.hide()
        self.deleteLater()

    def paintEvent(self, event):
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        color = self.__getColor()

        self.__drawBackground(painter, color)
        self.__drawText(painter, color)
        self.__drawFork(painter, color)
        self.__drawtipIcon(painter,color)

    def __drawtipIcon(self, painter: QPainter, color: ColorConfig):
        match self.status:
            case TipsStatus.Succeed:
                self.__drawHook(painter, color)
            case TipsStatus.Warning:
                self.__drawExclamation(painter, color)
            case TipsStatus.Dangerous:
                self.__drawInvalidation(painter, color)

    def __drawText(self, painter: QPainter, color: ColorConfig):
        painter.save()
        left_rect = self.__getLeftRect()
        text_rect = QRect(left_rect.width(), 0, self.width() - left_rect.width(), self.height()).adjusted(10, 0, 0, 0)

        pen = QPen()
        pen.setColor(color["text_color"])
        painter.setPen(pen)

        painter.setFont(self.font())

        textOption = QTextOption(Qt.AlignLeft | Qt.AlignVCenter)
        painter.drawText(text_rect, self.message, textOption)

        painter.restore()

    def __drawBackground(self, painter: QPainter, color: ColorConfig):
        painter.save()
        left_rect = self.__getLeftRect()

        below_rect = left_rect.adjusted(0, self.anim_y, 0, 0)
        top_rect = left_rect.adjusted(0, 0, 0, (left_rect.height() - self.anim_y))

        painter.setBrush(color["background_color"])
        painter.drawRect(self.rect())

        painter.setBrush(color["top_color"])
        painter.drawRect(top_rect)

        painter.setBrush(color["below_color"])
        painter.drawRect(below_rect)

        painter.restore()

    def __drawFork(self, painter: QPainter, color: ColorConfig):
        rect = self.__getRightRect()
        drawFork(painter,color["fork_color"],rect)

    def __drawHook(self, painter: QPainter, color: ColorConfig):
        rect = self.__getLeftRect()
        drawHook(painter,color["hook_color"],rect)

    def __drawExclamation(self, painter: QPainter, color: ColorConfig):
        rect = self.__getLeftRect()
        drawExclamation(painter,color["hook_color"],rect)

    def __drawInvalidation(self, painter: QPainter, color: ColorConfig):
        rect = self.__getLeftRect()
        drawInvalidation(painter,color["hook_color"],rect)

    def __getLeftRect(self) -> QRect:
        left_rect_size = QSize(32, self.height())
        left_rect = QRect(QPoint(0, 0), left_rect_size)
        return left_rect

    def __getRightRect(self) -> QRect:
        right_rect_size = QSize(32, self.height())
        left_rect = QRect(QPoint(self.width() - right_rect_size.width(), 0), right_rect_size)
        return left_rect

    def __getColor(self):
        if self.status == TipsStatus.Succeed:
            color_config: ColorConfig = {
                "hook_color": QColor(240, 240, 240),
                "fork_color": QColor(40, 134, 94),
                "text_color": QColor(54, 179, 126),
                "top_color": QColor(54, 179, 126),
                "below_color": QColor(40, 134, 94),
                "background_color": QColor(238, 250, 245),
            }
            return color_config
        elif self.status == TipsStatus.Dangerous:
            color_config: ColorConfig = {
                "hook_color": QColor(240, 240, 240),
                "fork_color": QColor(204, 51, 51),
                "text_color": QColor(220, 53, 69),
                "top_color": QColor(255, 102, 102),
                "below_color": QColor(204, 51, 51),
                "background_color": QColor(242, 222, 222),
            }
            return color_config
        elif self.status == TipsStatus.Warning:
            color_config: ColorConfig = {
                "hook_color": QColor(240, 240, 240),
                "fork_color": QColor(138, 118, 124),
                "text_color": QColor(193, 135, 59),
                "top_color": QColor(183, 157, 16),
                "below_color": QColor(128, 110, 17),
                "background_color": QColor(252, 248, 227),
            }
            return color_config

    def get_anim_range(self) -> Tuple:
        max_v = self.height()
        min_v = 0
        return min_v, max_v

    def onAnimParamChangeSignal(self, v) -> None:
        self.anim_y = v

    def __animShowRun(self):
        self.anim_show = QPropertyAnimation(self, b'geometry')

        self.anim_show.setDuration(120)
        self.anim_show.setEasingCurve(QEasingCurve.InOutSine)
        self.anim_show.setStartValue(QRect(self.pos(), QSize(self.width(), 0)))
        self.anim_show.setEndValue(QRect(self.pos(), QSize(self.width(), self.max_height)))

        self.anim_show.finished.connect(self.animForwardRun)
        self.anim.finished.connect(self.__fin)

        self.anim_show.start()

    def showEvent(self, event) -> None:
        QTimer.singleShot(0, lambda: self.__animShowRun())
        super().showEvent(event)

    def setText(self,text:str):
        self.message = text

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status:TipsStatus):
        self.__status = status



