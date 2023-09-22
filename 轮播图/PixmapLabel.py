
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QPixmap, QPainterPath, QPainter, QResizeEvent
from PySide6.QtWidgets import QLabel


class PixmapLabel(QLabel):
    """
        显示图片的Label组件，图片适应于组件大小，
        PixmapLabel会尽可能多地保留图片信息，
        组件尺寸发生变化，图片尺寸也会随之变化
        可以显示圆角图片，解决了图片覆盖Label圆角的问题
    """
    def __init__(self, *args, **kwargs):
        super(PixmapLabel, self).__init__(*args, **kwargs)
        self.pixmap_backup = None  # 保存未绘制的图片，防止尺寸多次变化后，图片失真


    def setStyleSheet(self, styleSheet: str) -> None:
        super(QLabel, self).setStyleSheet(styleSheet)

        # 提取圆角大小
        radius_match = QRegularExpression(r"border-radius:(?P<border_radius>\d+)px")
        radius_result = radius_match.match(styleSheet)
        if radius_result.hasMatch():
            self.border_radius = int(radius_result.captured("border_radius"))

    def __revPixmap(self, pixmap: QPixmap) -> QPixmap:
        """处理图片"""
        # 剪切后缩放
        cropped_pixmap = self.__crop_image_with_ratio(pixmap, self.width(), self.height())
        scaled_pixmap = self.__scale_pixmap(cropped_pixmap, self.width(), self.height())

        # 在新的 QPixmap 上绘制圆角图形
        rounded_pixmap = QPixmap(scaled_pixmap.size())
        rounded_pixmap.fill(Qt.transparent)

        # 创建带有圆角效果的图形路径
        rounded_rect = QPainterPath()
        rounded_rect.addRoundedRect(rounded_pixmap.rect(), self.border_radius, self.border_radius)

        # 绘制
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(rounded_rect)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        return rounded_pixmap

    def resizeEvent(self, event: QResizeEvent) -> None:
        """label缩小时，即时调整图片大小"""
        super(PixmapLabel, self).resizeEvent(event)
        if self.pixmap_backup is not None:
            # 重新调整图片大小
            pixmap = self.pixmap_backup
            pixmap = self.__revPixmap(pixmap)
            pixmap = self.__scale_pixmap(pixmap, self.width(), self.height())

            # 更新显示的图片
            super(PixmapLabel, self).setPixmap(pixmap)

    def setPixmap(self, pixmap: QPixmap, fun_count: int = 0) -> None:
        """设置图片"""
        if self.pixmap() is not None:
            self.pixmap_backup = pixmap
        pixmap = self.__revPixmap(pixmap)
        super(PixmapLabel, self).setPixmap(pixmap)

    def __scale_pixmap(self, pixmap: QPixmap, width: int, height: int) -> QPixmap:
        """缩放图片"""
        original_width = pixmap.width()
        original_height = pixmap.height()

        # 计算缩放比例
        scale_factor = max(width / original_width, height / original_height)

        # 缩放图片
        scaled_pixmap = pixmap.scaled(original_width * scale_factor, original_height * scale_factor)

        return scaled_pixmap

    def __crop_image_with_ratio(self, pixmap: QPixmap, width: int, height: int) -> QPixmap:
        """切割图片"""
        target_ratio = width / height
        original_width = pixmap.width()
        original_height = pixmap.height()

        # 计算裁剪区域的起点坐标和大小
        if original_width / original_height > target_ratio:
            # 如果原始宽高比大于目标比例，则以高度作为基准进行裁剪
            new_width = int(original_height * target_ratio)
            x = int((original_width - new_width) / 2)
            y = 0
            new_height = original_height
        else:
            # 如果原始宽高比小于目标比例，则以宽度作为基准进行裁剪
            new_height = int(original_width / target_ratio)
            x = 0
            y = int((original_height - new_height) / 2)
            new_width = original_width

        # 裁剪图片
        cropped_pixmap = pixmap.copy(x, y, new_width, new_height)

        return cropped_pixmap





