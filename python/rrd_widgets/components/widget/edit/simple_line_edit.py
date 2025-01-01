from typing import Tuple
from abc import abstractmethod

from PySide6.QtCore import Qt, QPointF, QEvent, QRect
from PySide6.QtGui import QColor, QPainter, QPen, QPainterPath, QResizeEvent

from ...base import LineEditAnimationBase


class SimpleLineEditBase(LineEditAnimationBase):
    def __init__(self, parent=None):
        super(SimpleLineEditBase, self).__init__(parent)
        self.border_radius: int = 0

        self.setFocusPolicy(Qt.ClickFocus)
        self.setProperty("transparent", True)

    @abstractmethod
    def setParams(self, font_color: QColor,background_color:QColor=QColor(255,255,255),*args):
        self.setStyleSheet(f"SimpleLineEditBase{{color:{font_color.name()};border:none;padding-left:5px;background"
                           f"-color:{background_color.name()};}}")
        pass

    def paintEvent(self, event:QEvent):
        super().paintEvent(event)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawForeground(painter)

    def drawForeground(self, painter):
        pass


class SimpleLineEdit_1(SimpleLineEditBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_foucus = False
        self.line_width_anim = 0
        self.anim_start_color: QColor = QColor()
        self.anim_finish_color: QColor = QColor()


    def setParams(self,
                  font_color: QColor,
                  anim_start_color: QColor = QColor(),
                  anim_finish_color: QColor = QColor(),
                  background_color: QColor = QColor(255, 255, 255),
                  border_radius: int = 10,
                  ):
        super().setParams(font_color,background_color)
        self.border_radius = 0
        self.anim_start_color = anim_start_color
        self.anim_finish_color = anim_finish_color

    def get_anim_range(self) -> Tuple:
        min_v = 0
        max_v = self.width()
        return min_v, max_v

    def drawForeground(self, painter: QPainter):
        painter.save()
        line_height = 2

        pen = QPen(QColor(self.anim_start_color), line_height, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, self.height() - line_height+1),
                         QPointF(self.width(), self.height() - line_height+1))

        if self.is_foucus:
            pen = QPen(QColor(self.anim_finish_color), line_height, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(QPointF(0, self.height() - line_height+1),
                             QPointF(self.line_width_anim, self.height() - line_height+1))
        painter.restore()

    def onAnimParamChangeSignal(self, v) -> None:
        self.line_width_anim = v

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.is_foucus = True
        self.animForwardRun()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.is_foucus = False
        self.animBackwardRun()

    def resizeEvent(self, event:QResizeEvent) -> None:
        super().resizeEvent(event)
        self.line_width_anim = event.size().width()

    def setGeometry(self, arg__1:QRect) -> None:
        super().setGeometry(arg__1)


class SimpleLineEdit_2(SimpleLineEditBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius = 0
        self.anim_start_color: QColor = QColor()
        self.anim_finish_color: QColor = QColor()

    def setParams(self,
                  font_color: QColor,
                  anim_start_color: QColor = QColor(),
                  anim_finish_color: QColor = QColor(),
                  border_radius: int = 10,
                  background_color: QColor = QColor(255, 255, 255),
                  ):
        super().setParams(font_color,background_color)
        self.border_radius = 0
        self.anim_start_color = anim_start_color
        self.anim_finish_color = anim_finish_color

    def drawForeground(self, painter: QPainter):
        painter.save()
        if not self.hasFocus():
            line_color = self.anim_start_color
        else:
            line_color = self.anim_finish_color
        line_width = 2

        pen = QPen(QColor(line_color), line_width, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, self.height() - line_width + 1),
                         QPointF(self.width(), self.height() - line_width + 1))
        painter.restore()

    def get_anim_range(self) -> Tuple:
        return 0, 0

    def resizeEvent(self, event:QResizeEvent) -> None:
        super().resizeEvent(event)
        self.line_width_anim = event.size().width()
