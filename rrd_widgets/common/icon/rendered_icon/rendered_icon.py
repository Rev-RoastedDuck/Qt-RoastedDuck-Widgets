from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen, QPainterPath, QColor


def drawFork(painter: QPainter, color: QColor,rect:QRect):
    painter.save()

    pen = QPen()
    pen.setWidth(2)
    pen.setColor(color)
    painter.setPen(pen)

    var = 5
    right_rect = rect
    x_center, y_certer = right_rect.x() + right_rect.width() // 2, right_rect.height() // 2

    path = QPainterPath()
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center + var, y_certer + var)
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center + var, y_certer - var)
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center - var, y_certer - var)
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center - var, y_certer + var)

    painter.drawPath(path)
    painter.restore()


def drawHook(painter: QPainter, color: QColor,rect:QRect):
    painter.save()

    left_rect = rect
    left_rect_size = left_rect.size()

    pen = QPen()
    pen.setWidth(2)
    pen.setColor(color)
    painter.setPen(pen)

    x_center, y_certer = left_rect_size.width() // 2 - 1, left_rect_size.height() // 2 + 5

    path = QPainterPath()
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center - 4, y_certer - 4)
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center + 8, y_certer - 10)

    painter.drawPath(path)
    painter.restore()


def drawExclamation(painter: QPainter, color: QColor,rect:QRect):
    painter.save()

    left_rect = rect
    left_rect_size = left_rect.size()
    x_center, y_certer = left_rect_size.width() // 2, left_rect_size.height() // 2 - 2

    pen = QPen()
    pen.setWidth(2)
    pen.setCapStyle(Qt.RoundCap)
    pen.setColor(color)
    painter.setPen(pen)

    painter.drawLine(x_center, y_certer - 5, x_center, y_certer + 5)

    pen.setWidth(3)
    painter.setPen(pen)
    painter.drawPoint(x_center, y_certer + 12)

    painter.restore()


def drawInvalidation(painter: QPainter, color: QColor,rect:QRect):
    painter.save()

    left_rect = rect
    left_rect_size = left_rect.size()
    x_center, y_certer = left_rect_size.width() // 2, left_rect_size.height() // 2
    r = 16

    pen = QPen()
    pen.setWidth(2)
    pen.setCapStyle(Qt.RoundCap)
    pen.setColor(color)
    painter.setPen(pen)

    painter.drawEllipse(x_center - r // 2, y_certer - r // 2, r, r)

    path = QPainterPath()
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center - 5, y_certer + 5)
    path.moveTo(x_center, y_certer)
    path.lineTo(x_center + 5, y_certer - 5)

    painter.drawPath(path)

    painter.restore()