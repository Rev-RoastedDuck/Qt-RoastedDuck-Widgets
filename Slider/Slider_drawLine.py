from PySide6.QtWidgets import QApplication, QWidget, QSlider
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QPen,QMouseEvent
from PySide6.QtCore import Qt, QRect, QPoint, QSize

"""drawLine实现"""
class Silder(QSlider):
    def __init__(self, orientation: Qt.Orientation, parent=None, ):
        super().__init__(orientation, parent=parent)
        self.__is_hovering_handle = False
        self.__is_pressed_handle = False
        self.__pressedPos = 0
        self.__paramsConfig()

        self.setMouseTracking(True)

    def __paramsConfig(self):
        # 颜色
        self.__color_groove_add = QColor(231, 227, 228)
        self.__color_groove_sub = QColor(148, 59, 142)
        self.__color_handle_outside = QColor(QColor(255, 255, 255))
        self.__color_handle_inside = QColor(QColor(148, 59, 142))

        # 线宽
        self.__width_line = 6

        # padding
        self.__padding = 15

        # handle 半径
        self.radius_handle = 10




    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        self.__paintGroove(painter)
        self.__paintHandle(painter)

    def __paintGroove(self, painter: QPainter):
        painter.save()

        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(self.__width_line)
        pen.setColor(self.__color_groove_add)

        painter.setPen(pen)

        if self.orientation() == Qt.Orientation.Horizontal:
            painter.drawLine(QPoint(self.__padding, self.__padding),
                             QPoint(self.width() - self.__padding * 2, self.__padding))
        else:
            painter.drawLine(QPoint(self.__padding, self.height() - self.__padding * 2),
                             QPoint(self.__padding, self.__padding))

        if self.value():
            args = self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()
            xy = int(((args - self.__padding * 2) / (self.maximum() - self.minimum())) * (self.value() - self.minimum()) + self.__padding)
            xy = xy if xy <= args - self.__padding else args - self.__padding

            pen.setColor(self.__color_groove_sub)
            painter.setPen(pen)

            if self.orientation() == Qt.Orientation.Horizontal:
                painter.drawLine(QPoint(self.__padding, self.__padding), QPoint(xy, self.__padding))
            else:
                painter.drawLine(QPoint(self.__padding, self.__padding),QPoint(self.__padding, xy))

        painter.restore()

    def __paintHandle(self, painter: QPainter):
        painter.save()

        point = self.__getHandlePos()

        if self.__is_hovering_handle:
            radius_big = self.radius_handle + 3
            radius_little = int(self.radius_handle * 0.6)
        else:
            radius_big = self.radius_handle
            radius_little = int(self.radius_handle * 0.6)
        # 外圆部分
        painter.setBrush(self.__color_handle_outside)
        painter.drawEllipse(point, radius_big, radius_big)

        # 内圆部分
        painter.setBrush(self.__color_handle_inside)
        painter.drawEllipse(point, radius_little, radius_little)

        painter.restore()

    def mousePressEvent(self, e: QMouseEvent):
        self.__pressedPos = e.position()
        self.setValue(self.__getCurrentValue(e.position()))
        self.__is_pressed_handle = True

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
        return int(pos_value * per)

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
