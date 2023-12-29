from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QFrame, QGraphicsBlurEffect
from PySide6.QtGui import QColor, QPainter, QPainterPath, QLinearGradient, QImage

from rrd_widgets.common.get_style_property import get_property, transfer_type
from rrd_widgets.common.set_blur_to_image import set_blur_to_image


class ShimmerButton(QFrame):
    def __init__(self, parent=None):
        super(ShimmerButton, self).__init__(parent)
        self.is_hover = False
        self.index = 0

    def setParams(self,
                  shimmer_color_1: QColor = None,
                  shimmer_color_2: QColor = None,
                  shimmer_blur_radius: int = None,
                  timer_interval: int = 5
                  ):
        """
        :param shimmer_color_1: 渐变颜色1
        :param shimmer_color_2: 渐变颜色2
        :param shimmer_blur_radius: 微光扩散程度
        :param timer_interval: 微光流动时间间隔，数值越小，流动速度越快
        """
        self.blur_radius = shimmer_blur_radius
        self.shimmer_color_1 = shimmer_color_1
        self.shimmer_color_2 = shimmer_color_2
        self.timer_interval = timer_interval

    def setAnimParams(self):
        """ 配置动画参数 """
        self.timer = QTimer()
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(self.offsetUpdate)

        self.rect_1_offset = self.width()  # 矩形1的坐标
        self.rect_2_offset = self.width()  # 矩形2的坐标
        self.rect_1_start = -self.width()  # 矩形1初始位置
        self.rect_2_start = -self.width() * 2  # 矩形2初始位置
        self.flag = 0  # 矩形1的初始位置标志，0 -> 矩形1在矩形1初始位置  1 -> 矩形1在默认初始位置

    def compSizeParams(self):
        """ 计算位置参数 """
        blur_radius_offset = 10
        self.foreground_width = self.width() - self.blur_radius - blur_radius_offset
        self.foreground_height = self.height() - self.blur_radius - blur_radius_offset

        self.background_width = self.width() - self.blur_radius - blur_radius_offset
        self.background_height = self.height() - self.blur_radius - blur_radius_offset

    def getStyleSheetParams(self):
        """ 提取样式 """
        ShimmerButtonBox_property: dict = get_property(self)["ShimmerButton"]
        self.font_color = transfer_type(ShimmerButtonBox_property["color"], "color")
        self.border_radius = transfer_type(ShimmerButtonBox_property["border-radius"], "pixel")

    def setGeometry(self, g):
        super(ShimmerButton, self).setGeometry(g)
        self.compSizeParams()

    def setStyleSheet(self, styleSheet: str) -> None:
        super(ShimmerButton, self).setStyleSheet(styleSheet)
        self.getStyleSheetParams()

    def paintEvent(self, event):
        super(ShimmerButton, self).paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter_widget = QPainter(self)
        painter_widget.setPen(Qt.NoPen)
        painter_widget.setClipPath(path)
        painter_widget.setRenderHint(QPainter.Antialiasing)

        # 绘制背景
        if self.is_hover:
            background = self.paintBackground()
            painter_widget.drawImage(self.background_x, self.background_y, background)

        foreground = self.paintForeground()
        painter_widget.drawImage(self.foreground_x, self.foreground_y, foreground)

        # 绘制文字
        self.paintText()

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

        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def paintBackground(self):
        """生成背景图片"""
        self.background_x = 0
        self.background_y = 0

        image_1_x = (self.width() - self.background_width) // 2
        image_1_y = (self.height() - self.background_height) // 2

        path_1 = QPainterPath()
        path_1.addRoundedRect(image_1_x, image_1_y, self.background_width, self.background_height, self.border_radius,
                              self.border_radius)

        image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path_1)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient_1 = self.createGradient(self.rect_1_start + self.rect_1_offset)
        painter.setBrush(gradient_1)
        painter.drawRect(self.rect_1_start + self.rect_1_offset, 0, self.width() + 1, self.height())

        gradient_2 = self.createGradient(self.rect_2_start + self.rect_2_offset)
        painter.setBrush(gradient_2)
        painter.drawRect(self.rect_2_start + self.rect_2_offset, 0, self.width() + 1, self.height())

        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(self.blur_radius)
        image_blur = set_blur_to_image(image, blur)

        painter.end()

        return image_blur

    def paintForeground(self):
        """生成前景图片"""
        self.foreground_x = (self.width() - self.foreground_width) // 2
        self.foreground_y = (self.height() - self.foreground_height) // 2

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.foreground_width, self.foreground_height, self.border_radius, self.border_radius)

        image = QImage(self.foreground_width, self.foreground_height, QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient_1 = self.createGradient(self.rect_1_start + self.rect_1_offset)
        painter.setBrush(gradient_1)
        painter.drawRect(self.rect_1_start + self.rect_1_offset, 0, self.width() + 1, self.height())

        gradient_2 = self.createGradient(self.rect_2_start + self.rect_2_offset)
        painter.setBrush(gradient_2)
        painter.drawRect(self.rect_2_start + self.rect_2_offset, 0, self.width() + 1, self.height())

        painter.end()
        return image

    def createGradient(self, x):
        '''
        设置渐变颜色
        :param x: 矩形的横坐标
        :return:
        '''
        gradient = QLinearGradient(x, 0, x + self.width(), 0)
        gradient.setColorAt(0, QColor(self.shimmer_color_1))
        gradient.setColorAt(0.5, QColor(self.shimmer_color_2))
        gradient.setColorAt(1, QColor(self.shimmer_color_1))

        return gradient

    def enterEvent(self, event):
        self.timer.start()
        self.is_hover = True

    def leaveEvent(self, event):
        self.timer.stop()
        self.is_hover = False
        self.update()

    def showEvent(self, event):
        super(ShimmerButton, self).showEvent(event)
        self.setAnimParams()

    def offsetUpdate(self):
        '''
        判断矩形是否离开按钮，并触发更新事件
        :return:
        '''
        if self.rect_1_offset >= self.width() * 2:
            self.rect_1_offset = 0
        if self.rect_2_offset >= self.width() * 3:
            self.rect_2_offset = 0
            self.rect_2_start = -self.width()
            self.flag = 1
        if self.rect_2_offset >= self.width() * 2 and self.flag == 1:
            self.rect_2_offset = 0

        self.rect_1_offset += 1
        self.rect_2_offset += 1

        self.update()

    def setText(self, text):
        self.text = text

    def mousePressEvent(self, event):
        """用于切换渐变色，此方法可删除"""
        self.color = [["#e83f97", "#f3a768"], ["#fbe74a", "#92d692"], ["#5bc9b9", "#92d692"], ["#4FFBDF", "#845EC2"],
                      ["#95d9ea", "#e5aae9"], ["#004d65", "#008d89"], ["#bb00ff", "#00b3ff"]]
        super(ShimmerButton, self).mousePressEvent(event)
        self.shimmer_color_1 = self.color[self.index][0]
        self.shimmer_color_2 = self.color[self.index][1]
        self.index += 1
        if self.index % len(self.color) == 0:
            self.index = 0
        self.update()



