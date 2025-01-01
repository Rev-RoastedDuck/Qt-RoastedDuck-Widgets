from PySide6.QtCore import QPoint, QRectF, Qt, QTimer
from PySide6.QtGui import QBrush, QPainter, QColor, QPen, QPainterPath

from ...base import ButtonAnimationBase

class SimpleButtonBase(ButtonAnimationBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.border_radius:int = 0
        self.full_color:QColor = QColor()
        self.font_color:QColor = QColor()

    def setParams(self,
                  text: str,
                  full_color: QColor,
                  font_anim_start_color: QColor,
                  font_anim_finish_color: QColor,
                  border_radius: int = 5,
                  ):
        """
        :param text: showed text
        :param full_color: color used to fill button
        :param font_anim_start_color: font color when mouse is not hovering
        :param font_anim_finish_color:font color when mouse is hovering
        :param border_radius: border radius of button
        :param timer_interval:timer interval for each frame of animation
        :return:
        """
        self.setText(text)
        self.full_color = full_color
        self.border_radius = border_radius
        self.font_anim_start_color = font_anim_start_color
        self.font_anim_finish_color = font_anim_finish_color

        self.font_color = self.font_anim_start_color

    def __drawText(self,painter:QPainter):
        """ 绘制文字 """
        painter.save()
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))

        if self.text():
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.restore()

    def drawBorder(self,painter:QPainter):
        pass

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        self.drawBorder(painter)
        self.drawForeground(painter)
        self.__drawText(painter)

    def drawForeground(self, painter: QPainter):
        pass

class SimpleButton14Base(SimpleButtonBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_enter = False

    def drawBorder(self,painter:QPainter):
        painter.save()
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(self.full_color)

        painter.setPen(pen)
        painter.drawRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.restore()

    def enterEvent(self, event):
        self.is_enter = True
        self.font_color = self.font_anim_finish_color
        self.animForwardRun()

    def leaveEvent(self, event):
        self.is_enter = False
        self.font_color = self.font_anim_start_color
        self.animBackwardRun()


class SimpleButton_1(SimpleButton14Base):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 0

    def get_anim_range(self):
        min = 0
        max = (self.width() ** 2 + self.height() ** 2) ** 0.5
        return min, max

    def drawForeground(self, painter: QPainter):
        painter.save()
        brush = QBrush(self.full_color)
        painter.setBrush(brush)

        painter.drawEllipse(QPoint(0, 0), self.radius, self.radius)
        painter.drawEllipse(QPoint(self.width(), self.height()), self.radius, self.radius)
        painter.restore()

    def onAnimParamChangeSignal(self, v):
        self.radius = v

class SimpleButton_2(SimpleButton14Base):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rect_width = 0

    def drawForeground(self,painter:QPainter):
        painter.save()
        brush = QBrush(self.full_color)
        painter.setBrush(brush)

        painter.translate(self.width() // 2, self.height() // 2)
        painter.rotate(45)
        painter.drawRect(QRectF(-self.rect_width // 2, -self.width() // 2, self.rect_width, self.width()))

        painter.restore()

    def onAnimParamChangeSignal(self, v):
        self.rect_width = v

    def get_anim_range(self):
        min = 0
        max = (self.width() ** 2 + self.height() ** 2) ** 0.5
        return min, max

class SimpleButton_3(SimpleButton14Base):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 0
        self.radius_delta_xy = 15  # 椭圆xy半径的差值

    def drawForeground(self,painter:QPainter):
        painter.save()
        painter.setBrush(self.full_color)
        painter.translate(self.width() // 2, int(self.height() * 1.5))

        radius_x = self.radius
        radius_y = self.radius - self.radius_delta_xy
        painter.drawEllipse(QPoint(0, 0), radius_x, radius_y)
        painter.restore()

    def onAnimParamChangeSignal(self, v):
        self.radius = v

    def get_anim_range(self):
        min = 0
        max = (self.width() ** 2 + self.height() ** 2) ** 0.5
        return min, max

class SimpleButton_4(SimpleButton14Base):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.rect_width = 0


    def drawForeground(self,painter:QPainter):
        painter.save()
        brush = QBrush(self.full_color)
        painter.setBrush(brush)

        if self.is_enter:
            painter.drawRect(QRectF(0, 0, self.rect_width, self.height()))
        elif not self.is_enter:
            painter.translate(self.width(), self.height())
            painter.rotate(180)
            painter.drawRect(QRectF(0, 0, self.rect_width, self.height()))
        painter.restore()

    def onAnimParamChangeSignal(self, v):
        self.rect_width = v

    def get_anim_range(self):
        min = 0
        max = self.width()
        return min, max

class SimpleButton_5(SimpleButtonBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.anima_hight = 0
        self.is_enter = False

    def setParams(self,
                  color=None,
                  border_radius: int = 5,
                  first_text: str = None,
                  second_text: str = None,
                  first_background_color: QColor = None,
                  second_background_color: QColor = None,
                  ):
        """
        :param color: font color
        :param border_radius: border radius
        :param timer_interval: timer interval for each frame of animation
        :param first_text: text when mouse is not hovering
        :param second_text:text when mouse is hovering
        :param first_background_color:background_color when mouse is not hovering
        :param second_background_color:background_color when mouse is hovering
        :return:
        """
        self.font_color = color
        self.border_radius = border_radius

        self.first_text = first_text
        self.second_text = second_text
        self.first_background_color = first_background_color
        self.second_background_color = second_background_color



    def drawForeground(self,painter:QPainter):
        """ draw image when mouse is hovering"""
        painter.translate(0, -self.anima_hight)

        painter.save()
        brush = QBrush(self.first_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width(), self.height()))
        self.drawText(painter)
        painter.restore()

        painter.save()
        brush = QBrush(self.second_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, self.height(), self.width(), self.height()))
        self.drawText(painter)
        painter.restore()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.is_enter = True
        self.animForwardRun()
        QTimer.singleShot(self.anim_msecs+1000, lambda: self.__animFin())

    def __animFin(self):
        self.is_enter = False
        self.animBackwardRun()

    def leaveEvent(self, event):
        self.is_enter = False
        self.animBackwardRun()

    def onAnimParamChangeSignal(self, v):
        self.anima_hight = v

    def get_anim_range(self):
        min = 0
        max = self.height()
        return min, max

    def drawText(self, painter: QPainter):
        painter.save()
        painter.setFont(self.font())
        painter.setPen(self.font_color)

        if not self.is_enter:
            painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, self.first_text)
        else:
            painter.drawText(0, self.height(), self.width(), self.height(), Qt.AlignCenter, self.second_text)
        painter.restore()

class SimpleButton_6(SimpleButtonBase):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.second_text = ""
        self.first_text = ""
        self.second_background_color = QColor()
        self.first_background_color = QColor()
        self.anima_width = 0
        self.is_enter = False

    def drawForeground(self,painter:QPainter):
        """ draw image when mouse is hovering"""
        painter.translate(self.anima_width, 0)

        painter.save()
        brush = QBrush(self.first_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width(), self.height()))
        self.drawText(painter)
        painter.restore()

        painter.save()
        brush = QBrush(self.second_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(-self.width(), 0, self.width(), self.height()))
        self.drawText(painter)
        painter.restore()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.is_enter = True
        self.animForwardRun()
        QTimer.singleShot(self.anim_msecs+1000, lambda: self.__animFin())

    def __animFin(self):
        self.is_enter = False
        self.animBackwardRun()

    def leaveEvent(self, event):
        self.is_enter = False
        self.animBackwardRun()

    def onAnimParamChangeSignal(self, v):
        self.anima_width = v

    def get_anim_range(self):
        min = 0
        max = self.width()
        return min, max

    def drawText(self, painter: QPainter):
        painter.save()
        painter.setFont(self.font())
        painter.setPen(self.font_color)

        if self.is_enter:
            painter.drawText(-self.width(),0,self.width(),self.height(), Qt.AlignCenter, self.second_text)
        else:
            painter.drawText(0, 0,self.width(), self.height(), Qt.AlignCenter, self.first_text)
        painter.restore()


    def setParams(self,
                  color=None,
                  border_radius: int = None,
                  first_text: str = None,
                  second_text: str = None,
                  first_background_color: QColor = None,
                  second_background_color: QColor = None,
                  ):
        """
        :param color: font color
        :param border_radius: border radius
        :param timer_interval: timer interval for each frame of animation
        :param first_text: text when mouse is not hovering
        :param second_text:text when mouse is hovering
        :param first_background_color:background_color when mouse is not hovering
        :param second_background_color:background_color when mouse is hovering
        :return:
        """
        self.font_color = color
        self.border_radius = border_radius

        self.first_text = first_text
        self.second_text = second_text
        self.first_background_color = first_background_color
        self.second_background_color = second_background_color
