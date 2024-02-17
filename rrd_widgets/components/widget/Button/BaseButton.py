from PySide6.QtCore import QRect, Qt, QEvent
from PySide6.QtGui import QColor, QPainter, QPainterPath, QLinearGradient, QPixmap, QPen
from PySide6.QtWidgets import QPushButton


class BaseSignalButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.is_hovering = False
        self.is_clicked = False
        self.installEventFilter(self)

    def eventFilter(self, obj, event: QEvent):
        if obj == self:
            if event.type() == QEvent.Enter:
                self.is_hovering = True
            if event.type() == QEvent.Leave:
                self.is_hovering = False
            if event.type() == QEvent.MouseButtonRelease:
                self.is_clicked = True

        return super().eventFilter(obj, event)


class BaseParamsButton(BaseSignalButton):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.font_color = QColor()
        self.border_color = QColor()
        self.background_color = QColor()
        self.border_radius = 0

    def setParams(self,
                  font_color: QColor=QColor(),
                  border_color: QColor=QColor(),
                  background_color: QColor=QColor(),
                  border_radius: int = 0,
                  ):
        self.font_color = font_color
        self.border_color = border_color
        self.border_radius = border_radius
        self.background_color = background_color


class BaseButton(BaseParamsButton):
    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        self.drawBackground(painter)
        self.drawIcon(painter)
        self.drawText(painter)

    def drawIcon(self, painter: QPainter):
        painter.save()
        if self.icon():
            pixmap = self.icon().pixmap(self.height() * 0.7)
            painter.drawPixmap(self.height() * 0.15, self.height() * 0.15, pixmap)
        painter.restore()

    def drawText(self, painter: QPainter):
        painter.save()
        if self.text():
            painter.setFont(self.font())
            painter.setPen(QColor(self.font_color))
            painter.drawText(self.rect().adjusted(self.height()+5, 0, 0, 0), Qt.AlignLeft | Qt.AlignVCenter, self.text())
        painter.restore()

    def drawBackground(self, painter: QPainter):
        painter.save()
        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())


class BaseHoveringButton(BaseButton):
    def drawBackground(self, painter: QPainter):
        super().drawBackground(painter)
        painter.save()
        if self.is_hovering:
            self.background_color.setAlpha(255)
        else:
            self.background_color.setAlpha(200)
        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())
        painter.restore()


class BaseClickedButton(BaseButton):
    def drawBackground(self, painter: QPainter):
        super().drawBackground(painter)
        painter.save()
        if self.is_clicked:
            pen = QPen()
            pen.setColor(self.border_color)
            pen.setWidth(3)
            painter.setPen(pen)
            painter.drawLine(0, self.border_radius, 0, self.height() - self.border_radius)
            painter.restore()
        painter.restore()

class BaseClickedHoveringButton(BaseButton):
    def drawBackground(self, painter: QPainter):
        super().drawBackground(painter)
        painter.save()

        if self.is_hovering:
            self.background_color.setAlpha(255)
        else:
            self.background_color.setAlpha(200)

        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())

        if self.is_clicked:
            pen = QPen()
            pen.setColor(self.border_color)
            pen.setWidth(3)
            painter.setPen(pen)
            painter.drawLine(0, self.border_radius, 0, self.height() - self.border_radius)
            painter.restore()
        painter.restore()
