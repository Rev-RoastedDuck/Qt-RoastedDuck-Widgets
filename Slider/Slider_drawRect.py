from PySide6.QtWidgets import QApplication, QWidget, QSlider
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QMouseEvent, QLinearGradient
from PySide6.QtCore import Qt, QRect, QPoint, QSize

"""drawrect实现"""

class Silder(QSlider):
    def __init__(self, orientation: Qt.Orientation, parent=None, ):
        super().__init__(orientation, parent=parent)
        self.__is_hovering_handle = False
        self.__is_pressed_handle = False
        self.setMouseTracking(True)
        self.__paramsConfig()
        self.__pressedPos = 0

    def __paramsConfig(self):
        # 颜色
        self.__color_groove_sub = QColor(148, 59, 142)
        self.__color_groove_add = QColor(231, 227, 228)
        self.__color_handle_inside = QColor(QColor(148, 59, 142))
        self.__color_handle_outside = QColor(QColor(255, 255, 255))


        # 线宽
        self.__width_line = 10

        # padding
        self.__padding = 15

        # handle 半径
        self.radius_handle = 10

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHints(QPainter.SmoothPixmapTransform | QPainter.Antialiasing)

        self.__drawGroove(painter)
        self.__drawHandle(painter)

    def __createGradient(self):
        if self.orientation() == Qt.Orientation.Horizontal:
            gradient = QLinearGradient(10,10,self.width()-10,10)
            gradient.setColorAt(0, QColor("#943b8e"))
            gradient.setColorAt(0.5, QColor("#ca3fa1"))
            gradient.setColorAt(1, QColor("#ff42b3"))
        else:
            gradient = QLinearGradient(10,10,10,self.height() - 10)
            gradient.setColorAt(0, QColor("#943b8e"))
            gradient.setColorAt(0.5, QColor("#ca3fa1"))
            gradient.setColorAt(1, QColor("#ff42b3"))

        return gradient

    def __drawGroove(self, painter: QPainter):
        painter.save()

        painter.setBrush(self.__color_groove_add)
        if self.orientation() == Qt.Orientation.Horizontal:
            painter.drawRoundedRect(
                QRect(self.__padding, self.__padding - self.__width_line // 2, self.width() - self.__padding*2, self.__width_line),
                self.__width_line / 2, self.__width_line / 2)
        else:
            painter.drawRoundedRect(
                QRect(self.__padding - self.__width_line // 2, self.__padding, self.__width_line, self.height() - self.__padding*2),
                self.__width_line / 2, self.__width_line / 2)

        if self.value():
            args = self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()
            xy = int(((args - self.__padding * 2) / (self.maximum() - self.minimum())) * (self.value() - self.minimum()) + self.__padding)
            xy = xy if xy <= args - self.__padding else args - self.__padding

            gradient = self.__createGradient()
            painter.setBrush(gradient)

            if self.orientation() == Qt.Orientation.Horizontal:
                painter.drawRoundedRect(
                    QRect(self.__padding, self.__padding - self.__width_line // 2, xy-self.__padding, self.__width_line),
                    self.__width_line / 2, self.__width_line / 2)
            else:
                painter.drawRoundedRect(
                    QRect(self.__padding - self.__width_line // 2, self.__padding, self.__width_line, xy-self.__padding),
                    self.__width_line / 2, self.__width_line / 2)

        painter.restore()

    def __drawHandle(self, painter: QPainter):
        painter.save()

        point = self.__getHandlePos()

        if self.__is_hovering_handle:
            radius_big = self.radius_handle + 3
            radius_little = int(self.radius_handle * 0.6)
        else:
            radius_big = self.radius_handle
            radius_little = int(self.radius_handle * 0.6)

        painter.setBrush(self.__color_handle_outside)
        painter.drawEllipse(point, radius_big, radius_big)

        painter.setBrush(self.__color_handle_inside)
        painter.drawEllipse(point, radius_little, radius_little)

        painter.restore()

    def mousePressEvent(self, e: QMouseEvent):
        self.__is_pressed_handle = True
        self.__pressedPos = e.position()
        self.setValue(self.__getCurrentValue(e.position()))

    def mouseMoveEvent(self, e: QMouseEvent):
        # mouseMoveEvent不会调用update()
        if self.__is_pressed_handle:
            self.setValue(self.__getCurrentValue(e.position()))
            print(self.value())

        handle_rect = self.__getHandleRect()
        if handle_rect.contains(e.position().toPoint()):
            self.__is_hovering_handle = True
            self.update()
        else:
            self.__is_hovering_handle = False
            self.update()

    def leaveEvent(self, e):
        self.__is_hovering_handle = False
        self.__is_pressed_handle = False

    def mouseReleaseEvent(self, e):
        self.__is_pressed_handle = False

    def __getCurrentValue(self, pos: QPoint):
        pos_value = int((pos.x() if self.orientation() == Qt.Orientation.Horizontal else pos.y()) - self.__padding)
        slider_lenth = int(
            (self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()) - self.__padding * 2)
        per = (self.maximum() - self.minimum()) / slider_lenth
        return int(pos_value * per + self.minimum())

    def __getHandlePos(self):
        slider_lenth_var = int(
            (self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()) - self.__padding * 2)
        xy = int((self.value() - self.minimum())/ ((self.maximum() - self.minimum()) / slider_lenth_var) + self.__padding)

        if self.orientation() == Qt.Orientation.Horizontal:
            xy = xy if xy <= self.width() - self.__padding else self.width() - self.__padding
            return QPoint(xy, self.__padding)
        else:
            xy = xy if xy <= self.height() - self.__padding else self.height() - self.__padding
            return QPoint(self.__padding, xy)

    def __getHandleRect(self) -> QRect:
        pos = QPoint(self.__getHandlePos().x() - self.radius_handle, self.__getHandlePos().y() - self.radius_handle)
        size = QSize(self.radius_handle * 2, self.radius_handle * 2)

        return QRect(pos, size).adjusted(-10,-10,10,10)


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(300, 300)

    s = Silder(Qt.Orientation.Vertical, w)
    s.resize(30, 200)
    s.move(5, 5)

    s2 = Silder(Qt.Orientation.Horizontal, w)
    s2.setMinimum(10)
    s2.setMaximum(100)
    s2.resize(200, 30)
    s2.move(50, 5)
    w.show()
    app.exec()
