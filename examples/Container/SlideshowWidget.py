from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import SlideShowWidget

if __name__ == "__main__":
    app = QApplication()
    m = QWidget()
    m.setStyleSheet("background-color: #990033")
    m.setGeometry(100, 60, 1380, 600)

    # 轮播图配置
    # middel_widget_size: 中间图片的尺寸
    # lr_widget_size: 两侧图片的尺寸
    w = SlideShowWidget(m, middel_widget_size=QSize(450, 200), lr_widget_size=QSize(250, 150))

    # 添加需要展示的图片
    pixmapList = [QPixmap("moon_cake/1.jpg"), QPixmap("moon_cake/2.jpg"),
                  QPixmap("moon_cake/3.jpg"),]
    for pixmap in pixmapList:
        w.addPixmap(pixmap)
    # 设置SlideshowWidget的位置和大小
    w.setGeometry((m.width() - 700) // 2, (m.height() - 260) // 2, 700, 260)

    m.show()
    app.exec()