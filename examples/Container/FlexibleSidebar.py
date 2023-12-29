import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import FlexibleSidebarButton,FlexibleSidebar


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setGeometry(200, 100, 320, 400)
    w.setStyleSheet("background-color:#ffffff;")

    icon1 = QIcon()
    icon1.addFile(":/icon/\u56fe\u6807/\u5173\u95ed (1).png", QSize(), QIcon.Normal, QIcon.Off)
    icon2 = QIcon()
    icon2.addFile(":/icon/\u56fe\u6807/\u767b\u5f55.png", QSize(), QIcon.Normal, QIcon.Off)
    icon3 = QIcon()
    icon3.addFile(":/icon/\u56fe\u6807/\u786e\u8ba4\u5bc6\u7801.png", QSize(), QIcon.Normal, QIcon.Off)
    icon4 = QIcon()
    icon4.addFile(":/icon/\u56fe\u6807/\u4f1a\u5458\u6ce8\u518c\u767b\u5f55\u7ba1\u7406.png", QSize(), QIcon.Normal, QIcon.Off)
    icon5 = QIcon()
    icon5.addFile(":/icon/\u56fe\u6807/\u9a8c\u8bc1 \u9a8c\u8bc1\u7801.png", QSize(), QIcon.Normal, QIcon.Off)
    icon6 = QIcon()
    icon6.addFile(":/icon/\u56fe\u6807/\u5206\u4eab.png", QSize(), QIcon.Normal, QIcon.Off)


    font = QFont()
    font.setPointSize(10)

    sliderbar = FlexibleSidebar(w)
    sliderbar.setParams(53, 141, background_color=QColor(0, 89, 89, 200), border_radius=15)
    sliderbar.setGeometry(100, 40, 141, 271)

    btn_1 = FlexibleSidebarButton(text="Close", icon=icon1, parent=sliderbar)
    btn_2 = FlexibleSidebarButton(text="Enter", icon=icon2, parent=sliderbar)
    btn_3 = FlexibleSidebarButton(text="SetKey", icon=icon3, parent=sliderbar)
    btn_4 = FlexibleSidebarButton(text="Resign", icon=icon4, parent=sliderbar)
    btn_5 = FlexibleSidebarButton(text="Verify", icon=icon5, parent=sliderbar)
    btn_6 = FlexibleSidebarButton(text="Share", icon=icon6, parent=sliderbar)

    btn_1.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))
    btn_2.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))
    btn_3.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))
    btn_4.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))
    btn_5.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))
    btn_6.setParams(font_color=QColor(255,255,255),background_color=QColor(0,89,89))

    btn_1.setFont(font)
    btn_2.setFont(font)
    btn_3.setFont(font)
    btn_4.setFont(font)
    btn_5.setFont(font)
    btn_6.setFont(font)

    sliderbar.addWidget(btn_1)
    sliderbar.addWidget(btn_2)
    sliderbar.addWidget(btn_3)
    sliderbar.addWidget(btn_4)
    sliderbar.addWidget(btn_5)
    sliderbar.addWidget(btn_6)

    w.show()

    app.exec()