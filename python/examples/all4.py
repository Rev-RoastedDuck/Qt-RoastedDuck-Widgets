import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import FlexibleSidebarButton, DynamicBorderWidget
from rrd_widgets.common import resource
from rrd_widgets import FlexibleSidebar_Hover, FlexibleSidebar_Click


class Window_1(QWidget):
    def __init__(self):
        super(Window_1, self).__init__()
        self.setStyleSheet("background-color:#ffffff;")
        self.resize(650, 450)
        self.setWindowTitle("rrd-widget")
        self.setStyleSheet("background: #ffffff;")

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
        icon6.addFile(":/icon_svg/icon_svg/share-2.svg", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setPointSize(10)

        # -------- FlexibleSidebar_Click -------- #
        # ======================================= #
        sliderbar_1 = FlexibleSidebar_Click(self)
        sliderbar_1.setParams(39, 141,
                              border_radius=15,
                              both_sides_stretching=True,
                              background_color=QColor(0, 89, 89, 200))
        sliderbar_1.setGeometry(50, 80, 141, 271)
        sliderbar_1.btn.setText("More")
        sliderbar_1.btn.setParams(font_color=QColor(255, 255, 255), background_color=QColor(255, 255, 255, 0))

        btn_1 = FlexibleSidebarButton(text="Close", icon=icon1, parent=sliderbar_1)
        btn_2 = FlexibleSidebarButton(text="Enter", icon=icon2, parent=sliderbar_1)
        btn_3 = FlexibleSidebarButton(text="SetKey", icon=icon3, parent=sliderbar_1)
        btn_4 = FlexibleSidebarButton(text="Resign", icon=icon4, parent=sliderbar_1)
        btn_5 = FlexibleSidebarButton(text="Verify", icon=icon5, parent=sliderbar_1)
        btn_6 = FlexibleSidebarButton(text="Share", icon=icon6, parent=sliderbar_1)

        btn_1.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0))
        btn_2.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0)
                        )
        btn_3.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0)
                        )
        btn_4.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0)
                        )
        btn_5.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0))
        btn_6.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        border_color=QColor(255, 255, 255),
                        hovering_color=QColor(0, 80, 80),
                        background_color=QColor(0, 0, 0, 0))

        btn_1.setFont(font)
        btn_2.setFont(font)
        btn_3.setFont(font)
        btn_4.setFont(font)
        btn_5.setFont(font)
        btn_6.setFont(font)

        btn_1.clicked.connect(self.update_num)
        btn_2.clicked.connect(self.update_num)
        btn_3.clicked.connect(self.update_num)
        btn_4.clicked.connect(self.update_num)
        btn_5.clicked.connect(self.update_num)
        btn_6.clicked.connect(self.update_num)

        sliderbar_1.addWidget(btn_1, 0)
        sliderbar_1.addWidget(btn_2, 0)
        sliderbar_1.addWidget(btn_3, 0)
        sliderbar_1.addWidget(btn_4, 0)
        sliderbar_1.addWidget(btn_5, 0)
        sliderbar_1.addWidget(btn_6, 0)

        # -------- FlexibleSidebar_Hover -------- #
        # ======================================= #
        sliderbar_2 = FlexibleSidebar_Hover(self)
        sliderbar_2.setParams(39, 141,
                              border_radius=15,
                              both_sides_stretching=False,
                              background_color=QColor(0, 89, 89, 200))
        sliderbar_2.setGeometry(200, 90, 141, 245)

        btn_1 = FlexibleSidebarButton(text="Close", icon=icon1, parent=sliderbar_2)
        btn_2 = FlexibleSidebarButton(text="Enter", icon=icon2, parent=sliderbar_2)
        btn_3 = FlexibleSidebarButton(text="SetKey", icon=icon3, parent=sliderbar_2)
        btn_4 = FlexibleSidebarButton(text="Resign", icon=icon4, parent=sliderbar_2)
        btn_5 = FlexibleSidebarButton(text="Verify", icon=icon5, parent=sliderbar_2)
        btn_6 = FlexibleSidebarButton(text="Share", icon=icon6, parent=sliderbar_2)

        btn_1.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))
        btn_2.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))
        btn_3.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))
        btn_4.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))
        btn_5.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))
        btn_6.setParams(font_color=QColor(255, 255, 255), border_radius=5,
                        hovering_color=QColor(0, 80, 80),
                        border_color=QColor(255, 255, 255),
                        background_color=QColor(0, 0, 0, 0))

        btn_1.setFont(font)
        btn_2.setFont(font)
        btn_3.setFont(font)
        btn_4.setFont(font)
        btn_5.setFont(font)
        btn_6.setFont(font)

        btn_1.clicked.connect(self.update_num)
        btn_2.clicked.connect(self.update_num)
        btn_3.clicked.connect(self.update_num)
        btn_4.clicked.connect(self.update_num)
        btn_5.clicked.connect(self.update_num)
        btn_6.clicked.connect(self.update_num)


        sliderbar_2.addWidget(btn_1, 0)
        sliderbar_2.addWidget(btn_2, 0)
        sliderbar_2.addWidget(btn_3, 0)
        sliderbar_2.addWidget(btn_4, 0)
        sliderbar_2.addWidget(btn_5, 0)
        sliderbar_2.addWidget(btn_6, 0)

        # -------- DynamicBorderWidget -------- #
        # ======================================= #
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(100)

        self.card = DynamicBorderWidget(self)
        self.card.setGeometry(360, 60, 200, 300)
        self.card.setParams(border_radius=15,
                       border_width=4,
                       color_1=QColor(143, 0, 26),
                       color_2=QColor(255, 107, 107),
                       font_color=QColor(255, 255, 255),
                       inside_background_color=QColor(55, 125, 125),
                       )

        self.card.setFont(font)
        self.card.setText("1")

    def update_num(self):
        parent = self.sender().parent()
        num = 0
        for item in parent.children():
            if isinstance(item,FlexibleSidebarButton):
                num += 1
                if self.sender() == item:
                    self.card.setText(f"{num}")
                    break
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window_1()
    w.show()

    app.exec()
