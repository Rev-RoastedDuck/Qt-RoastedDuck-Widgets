from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainterPath, QPainter, QBrush
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QPushButton, QHBoxLayout, QLabel

from ....common.icon.rendered_icon.rendered_icon import drawHook


class CheckBoxButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius = 5
        self.is_clicked = False
        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QColor(208, 208, 208))
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter.setClipPath(path)
        painter.drawRoundedRect(self.rect(), self.border_radius, self.border_radius)

        if self.is_clicked:
            self.__drawBackground(painter)

    def __drawBackground(self, painter: QPainter):
        rect = self.rect()
        drawHook(painter, QColor(0, 129, 140), rect)

    def mousePressEvent(self, event) -> None:
        self.is_clicked = not self.is_clicked


class CheckboxLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)


class CheckboxWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.border_radius = 5
        self.background_color = QColor(255, 255, 255)

        self.__ui_init()
        self.__setShadow()

    def setParams(self, border_radius: int = 5,
                  background_color: QColor = QColor(255, 255, 255),
                  ):
        self.border_radius = border_radius
        self.background_color = background_color

    def __setShadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(2, 2)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(20, 20, 20, 30))
        self.setGraphicsEffect(shadow)

    def __ui_init(self):
        self.button = CheckBoxButton(self)
        self.label = CheckboxLabel(self)

        self.hbox = QHBoxLayout(self)
        self.hbox.setSpacing(3)
        self.hbox.setContentsMargins(3, 3, 3, 3)
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.label)

    def paintEvent(self, event) -> None:
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.__drawBackground(painter)

    def __drawBackground(self, painter: QPainter):
        painter.save()

        brush = QBrush(self.background_color)
        painter.setBrush(brush)
        painter.drawRect(self.rect())
        painter.restore()

    def setText(self, text: str):
        self.label.setText(text)

    def showEvent(self, event) -> None:
        super(CheckboxWidget, self).showEvent(event)
        h = int(self.height() * 0.7)
        self.button.setFixedSize(h,h)
