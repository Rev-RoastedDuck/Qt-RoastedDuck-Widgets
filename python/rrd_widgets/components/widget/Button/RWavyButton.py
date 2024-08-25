from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QCursor, QPainter, QPen, QPainterPath

from ...base import ButtonAnimationBase


class RWavyButtonBase(ButtonAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius: int = 0
        self.full_color: QColor = QColor()
        self.font_color: QColor = QColor()

    def setParams(self, *args):
        pass

    def drawText(self, painter: QPainter):
        painter.save()
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text():
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.restore()

    def drawBorder(self, painter: QPainter):
        painter.save()
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(self.full_color)

        painter.setPen(pen)
        painter.drawRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.restore()

    def paintEvent(self, event):
        # super().paintEvent(event)

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


class RWavyButton(RWavyButtonBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mouse_clicked_pos = None

    def setParams(self,
                  font_color: QColor,
                  full_color: QColor,
                  border_radius: int = 5
                  ):
        self.full_color = full_color
        self.font_color = font_color
        self.border_radius = border_radius

    def onAnimParamChangeSignal(self, v):
        self.radius = v

    def get_anim_range(self):
        min = 0
        max = (self.width() ** 2 + self.height() ** 2) ** 0.5
        return min, max

    def drawForeground(self, painter: QPainter):
        painter.save()

        if self.mouse_clicked_pos is None or self.is_leave and self.radius < 2:
            painter.restore()
            return

        painter.setBrush(self.full_color)
        painter.drawEllipse(self.mouse_clicked_pos, self.radius, self.radius)

        painter.restore()

    def enterEvent(self, event):
        self.is_leave = False
        self.mouse_clicked_pos = event.position()
        self.animForwardRun()

    def leaveEvent(self, event):
        self.is_leave = True
        self.mouse_clicked_pos = self.mapFromGlobal(QCursor.pos())
        self.animBackwardRun()
