from PySide6.QtGui import  QColor, QCursor, QPainter

from RWavyButtonBase import RWavyButtonBase

class RWavyButton(RWavyButtonBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mouse_clicked_pos = None

    def setParams(self,
                  font_color:QColor,
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

    def drawForeground(self,painter:QPainter):
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