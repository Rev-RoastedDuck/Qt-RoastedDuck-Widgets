import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import FlexibleSidebarButton, FlexibleSidebar
from rrd_widgets.common import resource
from rrd_widgets.components.container.FlexibleSidebar import FlexibleSidebar_Hover,FlexibleSidebar_Click


class Window_1(QWidget):
    def __init__(self):
        super(Window_1, self).__init__()
        self.setStyleSheet("background-color:#000000;")

        icon1 = QIcon()
        icon1.addFile(":/icon_svg/icon_svg/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(":/icon_svg/icon_svg/enter.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addFile(":/icon_svg/icon_svg/set-key.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4 = QIcon()
        icon4.addFile(":/icon_svg/icon_svg/resign.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5 = QIcon()
        icon5.addFile(":/icon_svg/icon_svg/verify.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6 = QIcon()
        icon6.addFile(":/icon_svg/icon_svg/share.svg", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setPointSize(10)

        sliderbar = FlexibleSidebar_Click(self)
        sliderbar.setParams(50, 141, background_color=QColor(0, 89, 89, 200), border_radius=15,
                            both_sides_stretching=False)
        sliderbar.setGeometry(150, 80, 141, 271)

        btn_1 = FlexibleSidebarButton(text="Close", icon=icon1, parent=sliderbar)
        btn_2 = FlexibleSidebarButton(text="Enter", icon=icon2, parent=sliderbar)
        btn_3 = FlexibleSidebarButton(text="SetKey", icon=icon3, parent=sliderbar)
        btn_4 = FlexibleSidebarButton(text="Resign", icon=icon4, parent=sliderbar)
        btn_5 = FlexibleSidebarButton(text="Verify", icon=icon5, parent=sliderbar)
        btn_6 = FlexibleSidebarButton(text="Share", icon=icon6, parent=sliderbar)

        btn_1.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_2.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_3.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_4.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_5.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_6.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))

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

class Window_2(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#000000;")

        icon1 = QIcon()
        icon1.addFile(":/icon_svg/icon_svg/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(":/icon_svg/icon_svg/enter.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addFile(":/icon_svg/icon_svg/set-key.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4 = QIcon()
        icon4.addFile(":/icon_svg/icon_svg/resign.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5 = QIcon()
        icon5.addFile(":/icon_svg/icon_svg/verify.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6 = QIcon()
        icon6.addFile(":/icon_svg/icon_svg/share.svg", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setPointSize(10)

        sliderbar = FlexibleSidebar_Hover(self)
        sliderbar.setParams(50, 141, background_color=QColor(0, 89, 89, 200), border_radius=15,
                            both_sides_stretching=False)
        sliderbar.setGeometry(150, 80, 141, 245)

        btn_1 = FlexibleSidebarButton(text="Close", icon=icon1, parent=sliderbar)
        btn_2 = FlexibleSidebarButton(text="Enter", icon=icon2, parent=sliderbar)
        btn_3 = FlexibleSidebarButton(text="SetKey", icon=icon3, parent=sliderbar)
        btn_4 = FlexibleSidebarButton(text="Resign", icon=icon4, parent=sliderbar)
        btn_5 = FlexibleSidebarButton(text="Verify", icon=icon5, parent=sliderbar)
        btn_6 = FlexibleSidebarButton(text="Share", icon=icon6, parent=sliderbar)

        btn_1.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_2.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_3.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_4.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_5.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))
        btn_6.setParams(font_color=QColor(255, 255, 255), background_color=QColor(0, 89, 89), border_radius=5,
                        border_color=QColor(255, 255, 255))

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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window_1()
    w.show()

    w1 = Window_2()
    w1.show()

    app.exec()
