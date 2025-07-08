from PySide6.QtCore import QRect, Qt, QEvent,QSize
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
            if event.type() == QEvent.HoverEnter:
                self.is_hovering = True
            if event.type() == QEvent.HoverLeave:
                self.is_hovering = False
            if event.type() == QEvent.MouseButtonRelease:
                if self.click_toggle_enabled:
                    self.is_clicked = not self.is_clicked
                else:
                    self.is_clicked = True
        return super().eventFilter(obj, event)


class BaseParamsButton(BaseSignalButton):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.border_radius = 0
        self.border_color = QColor()
        self.background_color = QColor()

        self.icon_flag = Qt.AlignLeft

        self.font_color = QColor()
        self.text_padding = (0, 0, 0, 0)  # top right botton left
        self.text_flag = Qt.AlignLeft | Qt.AlignVCenter

    def setParams(self,
                  font_color: QColor = QColor(),
                  background_color: QColor = QColor(),
                  border_radius: int = 0,
                  border_color: QColor = QColor(),
                  text_padding: tuple = (0, 0, 0, 0),
                  text_flag: Qt.AlignmentFlag = Qt.AlignLeft | Qt.AlignVCenter,
                  *args
                  ):
        self.text_flag = text_flag
        self.text_padding = text_padding

        self.font_color = font_color
        self.border_color = border_color
        self.border_radius = border_radius
        self.background_color = background_color

    def setIconParams(self,size:QSize = QSize(16,16),
                      flag:Qt.AlignmentFlag = Qt.AlignLeft):
        self.icon_flag = flag
        self.setIconSize(size)

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
            pixmap = self.icon().pixmap(self.iconSize())
            padding = self.height() * 0.15
            if self.icon_flag == Qt.AlignRight:
                painter.drawPixmap(self.width() - padding - pixmap.width(), padding, pixmap)
            else:
                painter.drawPixmap(padding, padding, pixmap)


        painter.restore()

    def drawText(self, painter: QPainter):
        painter.save()
        if self.text():
            painter.setFont(self.font())
            painter.setPen(QColor(self.font_color))
            if self.icon():
                self.text_flag = Qt.AlignLeft | Qt.AlignVCenter
                if self.icon_flag == Qt.AlignRight:
                    painter.drawText(self.rect().adjusted(self.text_padding[3],
                                                          self.text_padding[0],
                                                          self.width() - self.height() - self.text_padding[1],
                                                          -2 - self.text_padding[2]),
                                                          self.text_flag, self.text())
                else:
                    painter.drawText(self.rect().adjusted(self.height() + self.text_padding[3],
                                                          self.text_padding[0],
                                                          -self.text_padding[1],
                                                          -2 - self.text_padding[2]),
                                                          self.text_flag, self.text())
            else:
                self.text_flag = Qt.AlignVCenter
                painter.drawText(self.rect().adjusted(5+self.text_padding[3],
                                                      5+self.text_padding[0],
                                                      -5-self.text_padding[1],
                                                      -5-self.text_padding[2]), self.text_flag, self.text())
        painter.restore()

    def drawBackground(self, painter: QPainter):
        painter.save()
        painter.setBrush(self.background_color)
        painter.drawRect(self.rect())
        painter.restore()


class BaseHoveringButton(BaseButton):
    def setParams(self,
                  font_color: QColor = QColor(),
                  border_color: QColor = QColor(),
                  background_color: QColor = QColor(),
                  border_radius: int = 0,
                  text_padding: tuple = (0, 0, 0, 0),
                  text_flag: Qt.AlignmentFlag = Qt.AlignLeft | Qt.AlignVCenter,
                  hovering_color: QColor() = QColor(255, 255, 255)
                  ):
        super().setParams(font_color=font_color, border_color=border_color, background_color=background_color,
                          border_radius=border_radius, text_flag=text_flag)
        self.hovering_color = hovering_color
        self.text_padding = text_padding


    def drawBackground(self, painter: QPainter):
        super().drawBackground(painter)
        painter.save()
        if self.is_hovering:
            painter.setBrush(self.hovering_color)
        else:
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


class BaseClickedHoveringButton(BaseButton):
    def setParams(self,
                  **kwargs
                  ):
        self.hovering_color = kwargs.pop('hovering_color', QColor(255, 255, 255))
        super().setParams(**kwargs)

    def drawBackground(self, painter: QPainter):
        painter.save()

        if self.is_hovering:
            painter.setBrush(self.hovering_color)
        else:
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
