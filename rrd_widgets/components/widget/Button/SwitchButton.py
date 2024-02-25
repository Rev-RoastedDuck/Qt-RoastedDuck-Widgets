from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QToolButton, QWidget
from PySide6.QtCore import Qt, Property, QPoint, QPropertyAnimation, QRect, Signal


class SwitchButtonBase(QToolButton):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setCheckable(True)
        self._indicatorX = 0

        self.animaInit()

    def animaInit(self):
        self.slideAni = QPropertyAnimation(self, b'indicatorX')
        self.slideAni.setDuration(200)

    def animaParamsInit(self):
        self.start = self.height() // 2
        self.end = self.width() - 2 - self.start
        self._indicatorX = self.start

    def setParams(self):
        pass

    def toggle(self):
        self.setChecked(not self.isChecked())
        if self.isChecked():
            self.slideAni.setEndValue(self.end)
        else:
            self.slideAni.setEndValue(self.start)
        self.slideAni.start()

    def mouseReleaseEvent(self, event) -> None:
        super().mouseReleaseEvent(event)
        if self.isChecked():
            self.slideAni.setEndValue(self.end)
        else:
            self.slideAni.setEndValue(self.start)
        self.slideAni.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        self.paintBackground(painter)
        self.paintIndicator(painter)

    def paintBackground(self, painter: QPainter):
        pass

    def paintIndicator(self, painter: QPainter):
        pass

    @Property(float)
    def indicatorX(self):
        return self._indicatorX

    @indicatorX.setter
    def indicatorX(self, x):
        self._indicatorX = x
        self.update()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.animaParamsInit()


class SwitchButton_1(SwitchButtonBase):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.indicator_color = QColor()
        self.background_color = QColor()
        self.checked_background_color = QColor()

    def setParams(self,
                  indicator_color: QColor = QColor(255, 255, 255),
                  background_color: QColor = QColor(188, 188, 188),
                  checked_background_color: QColor = QColor(0, 89, 89),
                  checked_indicator_color: QColor = QColor(255,255,255)
                  ):
        self.indicator_color = indicator_color
        self.background_color = background_color
        self.checked_background_color = checked_background_color
        self.checked_indicator_color = checked_indicator_color

    def paintBackground(self, painter: QPainter):
        painter.save()
        r = self.height() // 2
        rect = QRect(1, 1, self.width() - 2, self.height() - 1)

        if not self.isChecked():
            painter.setBrush(self.background_color)
        else:
            painter.setBrush(self.checked_background_color)

        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, r, r)
        painter.restore()

    def paintIndicator(self, painter: QPainter):
        painter.save()
        r = self.height() // 3
        point = QPoint(int(self._indicatorX), 0)

        painter.translate(0, self.height() // 2)
        painter.setPen(Qt.NoPen)

        if self.isChecked():
            painter.setBrush(self.checked_indicator_color)
        else:
            painter.setBrush(self.indicator_color)

        painter.drawEllipse(point, r, r)
        painter.restore()


class SwitchButton_2(SwitchButtonBase):
    def setParams(self,
                  indicator_color: QColor = QColor(181, 181, 181),
                  background_color: QColor = QColor(181, 181, 181),
                  checked_background_color: QColor = QColor(255, 167, 38),
                  checked_indicator_color: QColor = QColor(255, 167, 38)
                  ):
        self.indicator_color = indicator_color
        self.background_color = background_color
        self.checked_background_color = checked_background_color
        self.checked_indicator_color = checked_indicator_color

    def paintBackground(self, painter: QPainter):
        painter.save()
        r = self.height() // 2
        rect = QRect(1, 1, self.width() - 2, self.height() - 2)

        pen = QPen()
        pen.setWidth(3)
        if self.isChecked():
            pen.setColor(self.checked_background_color)
            painter.setPen(pen)
        else:
            pen.setColor(self.background_color)
            painter.setPen(pen)

        painter.drawRoundedRect(rect, r, r)
        painter.restore()

    def paintIndicator(self, painter: QPainter):
        painter.save()
        r = self.height() // 3
        point = QPoint(int(self._indicatorX), 0)

        painter.translate(0, self.height() // 2)

        if self.isChecked():
            painter.setBrush(self.checked_indicator_color)
        else:
            painter.setBrush(self.indicator_color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(point, r, r)
        painter.restore()


class SwitchButton_3(SwitchButtonBase):
    def setParams(self,
                  indicator_color: QColor = QColor(255, 255, 255),
                  background_color: QColor = QColor(204, 204, 204),
                  checked_background_color: QColor = QColor(51, 102, 153, 200),
                  checked_indicator_color: QColor = QColor(51, 102, 153)
                  ):
        self.indicator_color = indicator_color
        self.background_color = background_color
        self.checked_background_color = checked_background_color
        self.checked_indicator_color = checked_indicator_color

    def paintBackground(self, painter: QPainter):
        painter.save()

        w = self.width() - self.width() // 3
        h = self.height() - self.height() // 3
        rect = QRect(-w // 2, -h // 2, w, h)
        r = h // 2

        painter.translate(self.width() // 2, self.height() // 2)

        if self.isChecked():
            painter.setBrush(self.checked_background_color)
        else:
            painter.setBrush(self.background_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, r, r)
        painter.restore()

    def paintIndicator(self, painter: QPainter):
        painter.save()
        r = (self.height() - self.height() // 3) // 2 + self.height() // 9
        point = QPoint(int(self._indicatorX), 0)

        painter.translate(0, self.height() // 2)

        if self.isChecked():
            painter.setBrush(self.checked_indicator_color)
        else:
            painter.setBrush(self.indicator_color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(point, r, r)
        painter.restore()


class SwitchButton_4(SwitchButtonBase):
    def animaParamsInit(self):
        super().animaParamsInit()
        self.isHover = False

    def setParams(self,
                  indicator_color: QColor = QColor(255, 255, 255),
                  background_color: QColor = QColor(204, 204, 204),
                  checked_background_color: QColor = QColor(153, 0, 51, 200),
                  checked_indicator_color: QColor = QColor(153, 0, 51)
                  ):
        self.indicator_color = indicator_color
        self.background_color = background_color
        self.checked_background_color = checked_background_color
        self.checked_indicator_color = checked_indicator_color

    def enterEvent(self, event):
        super().enterEvent(event)
        self.isHover = True

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.isHover = False

    def paintBackground(self, painter: QPainter):
        painter.save()

        w = self.width() - self.width() // 2
        h = self.height() - self.height() // 2

        r = h // 2

        painter.translate(self.width() // 2, self.height() // 2)

        rect = QRect(-w // 2, -h // 2, w, h)

        painter.setPen(Qt.NoPen)
        if self.isChecked():
            painter.setBrush(self.checked_background_color)
        else:
            painter.setBrush(self.background_color)

        painter.drawRoundedRect(rect, r, r)
        painter.restore()

    def paintIndicator(self, painter: QPainter):
        painter.save()
        r = (self.height() - self.height() // 2) // 2 + self.height() // 9
        point = QPoint(int(self._indicatorX), 0)

        painter.translate(0, self.height() // 2)
        painter.setPen(Qt.NoPen)
        if self.isChecked():
            if self.isHover:
                c = self.checked_indicator_color
                painter.setBrush(QColor(c.red(), c.green(), c.blue(), 100))
                painter.drawEllipse(point, r + 5, r + 5)
            painter.setBrush(self.checked_indicator_color)

        else:
            if self.isHover:
                c = self.indicator_color
                painter.setBrush(QColor(c.red(), c.green(), c.blue(), 100))
                painter.drawEllipse(point, r + 5, r + 5)
            painter.setBrush(self.indicator_color)

        painter.drawEllipse(point, r, r)

        painter.restore()


class SwitchButton_5(SwitchButtonBase):
    def setParams(self,
                  indicator_color: QColor = QColor(255, 255, 255),
                  background_color: QColor = QColor(204, 204, 204),
                  checked_background_color: QColor = QColor(153, 0, 51, 200),
                  ):
        self.indicator_color = indicator_color
        self.background_color = background_color
        self.checked_background_color = checked_background_color

    def animaParamsInit(self):
        self.var = self.height() // 8
        h = self.height() - self.var * 2
        self.start = self.var
        self.end = self.width() - h - self.var
        self._indicatorX = self.var

    def paintBackground(self, painter: QPainter):
        painter.save()
        if self.isChecked():
            painter.setBrush(self.checked_background_color)
        else:
            painter.setBrush(self.background_color)

        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 5, 5)
        painter.restore()

    def paintIndicator(self, painter: QPainter):
        painter.save()
        h = self.height() - self.var * 2
        rect = QRect(self._indicatorX, -h // 2, h, h)

        painter.translate(0, self.height() // 2)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.indicator_color)

        painter.drawRoundedRect(rect, 5, 5)
        painter.restore()

