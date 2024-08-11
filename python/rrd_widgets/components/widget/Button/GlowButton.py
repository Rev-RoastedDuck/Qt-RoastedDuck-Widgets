from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor, QPainter, QPainterPath, QLinearGradient, QPixmap

from ...base import ButtonAnimationBase

class GlowButton(ButtonAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.offset = 0
        self.anim_msecs = 1000

        self.border = None
        self.font_color = None
        self.border_radius = None
        self.pixmap: QPixmap = QPixmap()
    def setParams(self, border_radius: int,
                  border_width: int,
                  font_color: QColor
                  ):
        self.border = border_width
        self.font_color = font_color
        self.border_radius = border_radius

    def setBorder(self):
        btn_x = self.border
        btn_y = self.border
        btn_width = self.width() - self.border * 2
        btn_height = self.height() - self.border * 2
        return QRect(btn_x, btn_y, btn_width, btn_height)

    def paintEvent(self, event):
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.setBorder(), self.border_radius, self.border_radius)
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawForeground(painter)
        self.drawText(painter)

    def drawText(self, painter: QPainter):
        painter.save()
        path = QPainterPath()
        path.addRoundedRect(self.setBorder(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text():
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.restore()

    def drawForeground(self, painter: QPainter):
        painter.save()
        if not self.pixmap:
            self.pixmap = self.getForegroundPixmap()

        left_rect = QRect(0, 0, self.width() - self.offset, self.height())
        right_rect = QRect(self.width() - self.offset, 0, self.offset, self.height())

        left_pixmap = self.pixmap.copy(left_rect)
        right_pixmap = self.pixmap.copy(right_rect)

        painter.drawPixmap(0, 0, right_pixmap)
        painter.drawPixmap(self.offset, 0, left_pixmap)
        painter.restore()

    def getForegroundPixmap(self) -> QPixmap:
        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = self.createGradient(0)
        painter.setBrush(gradient)
        painter.drawRect(0, 0, self.width(), self.height())

        painter.end()

        return pixmap

    def createGradient(self, x):
        '''
        设置渐变颜色
        :param x: 矩形的横坐标
        :return:
        '''
        gradient = QLinearGradient(x, 0, x + self.width(), 0)
        gradient.setColorAt(0, QColor(0, 164, 128, 230))
        gradient.setColorAt(0.166, QColor(13, 88, 166, 230))
        gradient.setColorAt(0.333, QColor(118, 8, 170, 230))
        gradient.setColorAt(0.5, QColor(255, 144, 0, 230))
        gradient.setColorAt(0.666, QColor(255, 255, 0, 230))
        gradient.setColorAt(0.833, QColor(165, 239, 0, 230))
        gradient.setColorAt(1, QColor(83, 223, 0, 230))
        return gradient

    def loop_ani(self):
        self.anim_param = 0
        self.animForwardRun()

    def showEvent(self, event):
        super().showEvent(event)
        self.anim.finished.connect(self.loop_ani)

    def onAnimParamChangeSignal(self, v):
        self.offset = v

    def get_anim_range(self):
        min_v = 0
        max_v = self.width()
        return min_v, max_v

    def enterEvent(self, event):
        self.animForwardRun()

    def leaveEvent(self, event):
        self.anim.stop()

