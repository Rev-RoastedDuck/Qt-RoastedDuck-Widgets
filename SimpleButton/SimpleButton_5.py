from PySide6.QtCore import QRect, QSize, Qt, QTimer, QRegularExpression, QPoint, QRectF
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QPainter, QPainterPath, QIcon, QPen
from PySide6.QtWidgets import QApplication, QFrame, QPushButton,QWidget

class SimpleButton_5(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

    def setParams(self,
                  color=None,
                  border_radius: int = 5,
                  timer_interval: int = 10,
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
        self.timer_interval = timer_interval

        self.first_text = first_text
        self.second_text = second_text
        self.first_background_color = first_background_color
        self.second_background_color = second_background_color


    def animationConfig(self):
        self.anima_hight = 0
        self.anima_height_var = 8
        self.anima_max_height = self.height()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.incHeight)
        self.timer.setInterval(self.timer_interval)

        self.is_enter = False

    def paintText(self,painter:QPainter):
        painter.setFont(self.font())
        painter.setPen(self.font_color)

        if not self.is_enter:
            painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, self.first_text)
        else:
            painter.drawText(0, self.height(), self.width(), self.height(), Qt.AlignCenter, self.second_text)

    def paintImageInit(self,painter:QPainter):
        """ draw image when mouse is not hovering"""
        painter.save()
        brush = QBrush(self.first_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width(), self.height()))
        self.paintText(painter)
        painter.restore()

    def paintImage(self, painter:QPainter):
        """ draw image when mouse is hovering"""
        painter.translate(0, -self.anima_hight)

        painter.save()
        brush = QBrush(self.first_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width(), self.height()))
        self.paintText(painter)
        painter.restore()

        painter.save()
        brush = QBrush(self.second_background_color)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, self.height(), self.width(), self.height()))
        self.paintText(painter)
        painter.restore()

    def paintEvent(self, event):
        # super().paintEvent(event)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.paintImageInit(painter)
        self.paintImage(painter)

    def incHeight(self):
        self.anima_hight += self.anima_height_var
        if self.anima_hight > self.anima_max_height:
            self.anima_hight = self.anima_max_height
            self.timer.stop()
        self.update()

    def decHeight(self):
        self.anima_hight -= self.anima_height_var
        if self.anima_hight < 0:
            self.anima_hight = 0
            self.timer.stop()
        self.update()

    def enterEvent(self, event):
        self.is_enter = True

        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incHeight)
        self.timer.start()

    def leaveEvent(self, event):
        self.is_enter = False

        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decHeight)
        self.timer.start()

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self.animationConfig()


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background: #000000;")

    # 按钮样式配置
    btn = SimpleButton_5(w)
    btn.setGeometry(QRect(290, 280, 140, 45))
    btn.setParams(color = QColor("#ffffff"),
                  timer_interval = 18,
                  border_radius= 10,
                  first_text = "Hold that",
                  second_text ="Succeed",
                  first_background_color = QColor("#21dc62"),
                  second_background_color= QColor("#1e90ff"),
                  )
    # 设置字体
    font = QFont()
    font.setPointSize(13)
    btn.setFont(font)

    w.show()
    app.exec()