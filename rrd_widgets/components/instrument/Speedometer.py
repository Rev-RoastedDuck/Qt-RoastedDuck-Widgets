"""
Qt-RoastedDuck-Widgets
======================
Qt widgets-based implementation of the Material Design specification.

Repository at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.

Demo are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/Demo.

Examples are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/examples.

Information:
    WeChat: Roast_71.
    csdnBlog: https://blog.csdn.net/m0_72760466?type=blog.

:copyright: (c) 2023 by Rev-RoastedDuck.
:license: GPLv3, see LICENSE for more details.
"""
from typing import Any

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRect, QPoint, QSize
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QPen, QPainterPath, QBrush, QTextOption, QImage


class SpeedometerBase(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.text_h = 30  # 定义文本的高度
        self.text_y = -10  # 定义文本的位置
        self.text_unit = ""  # 定义文本的单位

        self.max_value = 0  # 定义最大数值
        self.min_value = 0  # 定义最小数值
        self.current_value = 0  # 定义当前数值

        self.radius: int = 0  # 定义组件半径
        self.angle_start = 0  # 定义起始角度
        self.angle_range = 180  # 定义角度范围
        self.pen_width_arc = 10  # 定义圆环宽度

        self.color_font: QColor = QColor()
        self.color_arc_add: QColor = QColor()
        self.color_arc_sub: QColor = QColor()
        self.color_triangle: QColor = QColor()

    def setParams(self, radius: int,
                  color_arc_add: QColor,
                  color_arc_sub: QColor,
                  color_triangle: QColor,
                  color_font: QColor,
                  text_unit: str = "",
                  text_y: int = 10,
                  text_height: int = 30,
                  ) -> None:
        """
        :param radius:          组件半径大小
        :param color_arc_add:   已覆盖区域的颜色
        :param color_arc_sub:   未覆盖区域的颜色
        :param color_triangle:  指针的颜色
        :param color_font:      文字的颜色
        :param text_unit:       文本的单位
        :param text_y:          文本的位置
        :param text_height:     文本的高度
        :return:
        """
        self.color_font = color_font
        self.color_arc_add = color_arc_add
        self.color_arc_sub = color_arc_sub
        self.color_triangle = color_triangle

        self.text_y = text_y
        self.text_h = text_height
        self.text_unit = text_unit

        self.radius = radius
        self.resize(QSize(int(radius * 2.5), int(radius * 1.8)))

    def __creatRadiusTriangle(self, num: int) -> int:
        range_radius_triangle = self.angle_range
        per = range_radius_triangle / (self.max_value - self.min_value)
        return int((num - self.min_value) * per)

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)

        painter = QPainter(self)
        painter.translate(self.size().width() // 2, int(self.radius * 1.2))
        painter.setRenderHints(QPainter.SmoothPixmapTransform | QPainter.Antialiasing)

        radius_of_triangle = self.__creatRadiusTriangle(self.current_value)
        self.__drawText(painter)
        self.__drawArc(painter, radius_of_triangle)
        self.drawTriangle(painter, radius_of_triangle)

    def __drawArc(self, painter: QPainter, val: int = 0) -> None:
        circ_rect = QRect(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

        painter.save()
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(self.pen_width_arc)
        pen.setColor(self.color_arc_add)
        painter.setPen(pen)

        painter.drawArc(circ_rect, self.angle_start * 16, self.angle_range * 16)
        if val:
            pen.setColor(self.color_arc_sub)
            painter.setPen(pen)
            painter.drawArc(circ_rect, -(self.angle_start + 180) * 16, -val * 16)

        painter.restore()

    def __drawText(self, painter: QPainter) -> None:
        painter.save()
        pen = QPen()
        pen.setColor(self.color_font)
        painter.setPen(pen)

        rect = QRect(-self.radius, self.text_y, self.radius * 2, self.text_h)
        text = str(self.current_value) + self.text_unit
        text_option = QTextOption(Qt.AlignCenter)
        painter.drawText(rect, text, text_option)
        painter.restore()

    def drawTriangle(self, painter: QPainter, radius_of_triangle: int = 0) -> None:
        pass

    def updateValue(self, value: Any) -> None:
        self.current_value = value
        self.update()

    def setRange(self, min: int, max: int) -> None:
        self.max_value = max
        self.min_value = min


class Speedometer1(SpeedometerBase):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def drawTriangle(self, painter: QPainter, radius_of_triangle: int = 0):
        painter.save()
        painter.rotate(radius_of_triangle + self.angle_start)

        brush = QBrush(self.color_triangle)
        painter.setBrush(brush)

        l_triangle = int(self.radius * 0.7)
        circle_radius_big = int(self.radius * 0.18)
        circle_radius_little = circle_radius_big // 2

        path_big_triangle = QPainterPath()
        path_big_triangle.arcTo(
            QRect(-circle_radius_big, -circle_radius_big, circle_radius_big * 2, circle_radius_big * 2), -90, 180)
        path_big_triangle.lineTo(QPoint(-l_triangle, 0))
        path_big_triangle.lineTo(QPoint(0, circle_radius_big))

        path_little_circle = QPainterPath()
        path_little_circle.arcTo(
            QRect(-circle_radius_little, -circle_radius_little, circle_radius_little * 2, circle_radius_little * 2), 0,
            360)

        path_subed = path_big_triangle.subtracted(path_little_circle)
        painter.drawPath(path_subed)

        painter.restore()


class Speedometer2(SpeedometerBase):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.pen_width_arc = 10

    def drawTriangle(self, painter: QPainter, radius_of_triangle: int = 0):
        painter.save()
        painter.rotate(radius_of_triangle + self.angle_start)

        circle_radius_big = int(self.radius * 0.18)
        circle_radius_little = circle_radius_big // 2

        path_big_circle = QPainterPath()
        path_big_circle.moveTo(-self.radius, 0)
        path_big_circle.arcTo(
            QRect(-circle_radius_big - self.radius, -circle_radius_big, circle_radius_big * 2, circle_radius_big * 2),
            0,
            360)
        brush = QBrush(self.color_triangle)
        painter.setBrush(brush)
        painter.drawPath(path_big_circle)

        path_little_circle = QPainterPath()
        path_little_circle.moveTo(-self.radius + circle_radius_little, 0)
        path_little_circle.arcTo(
            QRect(-circle_radius_little - self.radius, -circle_radius_little, circle_radius_little * 2,
                  circle_radius_little * 2), 0,
            361)
        brush = QBrush(self.color_arc_add)
        painter.setBrush(brush)
        painter.drawPath(path_little_circle)

        painter.restore()


class Speedometer3(SpeedometerBase):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.pen_width_arc = 20

    def drawTriangle(self, painter: QPainter, radius_of_triangle: int = 0):
        painter.save()
        painter.rotate(radius_of_triangle + self.angle_start)

        circle_radius_big = int(self.radius * 0.18)
        circle_radius_little = circle_radius_big // 2

        path_big_circle = QPainterPath()
        path_big_circle.moveTo(-self.radius, 0)
        path_big_circle.arcTo(
            QRect(-circle_radius_big - self.radius, -circle_radius_big, circle_radius_big * 2, circle_radius_big * 2),
            0,
            360)
        brush = QBrush(self.color_triangle)
        painter.setBrush(brush)
        painter.drawPath(path_big_circle)

        path_little_circle = QPainterPath()
        path_little_circle.moveTo(-self.radius + circle_radius_little, 0)
        path_little_circle.arcTo(
            QRect(-circle_radius_little - self.radius, -circle_radius_little, circle_radius_little * 2,
                  circle_radius_little * 2), 0,
            361)
        brush = QBrush(self.color_arc_add)
        painter.setBrush(brush)
        painter.drawPath(path_little_circle)

        painter.restore()



