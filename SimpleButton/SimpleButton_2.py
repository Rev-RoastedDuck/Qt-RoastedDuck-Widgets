from PySide6.QtCore import QRect, QSize, Qt, QTimer, QRegularExpression, QPoint, QRectF
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QPainter, QPainterPath, QIcon
from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QWidget

"""
2023/9/13 

"""


class SimpleButton_2(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text = ""

    def setParams(self,
                  text: str,
                  full_color: QColor,
                  font_anim_start_color: QColor,
                  font_anim_finish_color: QColor,
                  border_radius: int = 5,
                  timer_interval: int = 10,
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
        self.text = text
        self.full_color = full_color
        self.border_radius = border_radius
        self.timer_interval = timer_interval
        self.font_anim_start_color = font_anim_start_color
        self.font_anim_finish_color = font_anim_finish_color

        self.font_color = self.font_anim_start_color

        border_color = self.full_color.name()
        self.setStyleSheet("SimpleButton_2{"
                           f"    border:1px solid  {border_color};"
                           "    background-color: rgba(0, 0, 0,0);"
                           f"    border-radius:{self.border_radius}px;"
                           "}"
                           )

    def animationConfig(self):
        self.recr_width = 0
        self.rect_width_var = 5
        self.rect_max_width = (self.width() ** 2 + self.height() ** 2) ** 0.5

        self.timer = QTimer(self)
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(self.incWidth)

    def incWidth(self):
        self.recr_width += self.rect_width_var
        if self.recr_width > self.rect_max_width:
            self.timer.stop()
            return
        self.update()

    def decWidth(self):
        self.recr_width -= self.rect_width_var
        if self.recr_width < 0:
            self.timer.stop()
            return
        self.update()

    def setText(self, text):
        self.text = text

    def paintText(self):
        """ 绘制文字 """
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setFont(self.font())
        painter.setPen(QColor(self.font_color))
        painter.setRenderHint(QPainter.Antialiasing)

        if self.text:
            painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(self.full_color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)

        painter.translate(self.width() // 2, self.height() // 2)  # 将画笔移动到矩阵中心
        painter.rotate(45)  # 将坐标系旋转45度
        painter.drawRect(QRectF(-self.recr_width // 2, -self.width() // 2, self.recr_width, self.width()))

        self.paintText()

    def enterEvent(self, event):
        self.font_color = self.font_anim_finish_color
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.incWidth)
        self.timer.start()

    def leaveEvent(self, event):
        self.font_color = self.font_anim_start_color
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.decWidth)
        self.timer.start()

    def showEvent(self, event):
        super().showEvent(event)
        self.animationConfig()

    def setStyleSheet(self, styleSheet):
        super().setStyleSheet(styleSheet)


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800, 800)
    w.setStyleSheet("background: #000000;")

    # 按钮样式配置
    btn = SimpleButton_2(w)
    btn.setGeometry(QRect(290, 280, 140, 45))
    btn.setParams(text="Hold That",
                  border_radius=5,
                  timer_interval=8,
                  full_color=QColor("#00A97F"),
                  font_anim_start_color=QColor("#00A97F"),
                  font_anim_finish_color=QColor("#ffffff"),
                  )
    # 设置字体
    font = QFont()
    font.setPointSize(13)
    btn.setFont(font)

    w.show()
    app.exec()
