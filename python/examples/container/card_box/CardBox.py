from rrd_widgets import BaseHoveringButton

from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtCore import QRect, Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from rrd_widgets.components.container.card_box import CardBoxDeletable

import icon
from CardBoxUI import Ui_Form


class CardWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.uiInit()

    def uiInit(self):
        # 卡片样式
        self.setGeometry(QRect(350, 240, 171, 221))
        self.setObjectName(u"card")
        self.setMinimumSize(QSize(171, 221))
        self.setMaximumSize(QSize(171, 221))
        self.setStyleSheet("""
        #card{
            background:rgb(233, 228, 237);
            border-radius:10px;
        }
        """)

        # 垂直布局器
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # 卡片顶部
        # 删除按钮 卡片顶部水平布局器中
        self.delPushButton = QPushButton(self)
        self.delPushButton.setIconSize(QSize(20, 20))
        self.delPushButton.setMinimumSize(QSize(25, 25))
        self.delPushButton.setIcon(QIcon(":/icon/icon_raw/删除.svg"))

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout.addStretch(1)
        self.horizontalLayout.addWidget(self.delPushButton)

        # 添加顶部内容到整体(卡片)垂直布局器
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 卡片内容部分
        self.main_widget = QWidget(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_widget)

        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)

        # comboBox_data_pos
        self.ui.comboBox_data_pos.setItemParams(color_font=QColor(0, 0, 0),
                                                border_radius=2,
                                                color_hover=QColor(0, 0, 0, 35),
                                                color_background=QColor(245, 243, 247),
                                                color_border=QColor(101, 60, 147),
                                                item_spacing=2,
                                                item_height=20,
                                                )

        self.ui.comboBox_data_pos.setParams(border_radius=5,
                                            font_color=QColor(0, 0, 0),
                                            background_color=QColor(245, 243, 247)
                                            )
        self.ui.comboBox_data_pos.setFont(font)
        self.data_pos = ["数据头", "数据尾", "数据体", "长度校验", "大小校验"]
        self.ui.comboBox_data_pos.addItems(self.data_pos)

        # comboBox_data_type
        self.ui.comboBox_data_type.setItemParams(color_font=QColor(0, 0, 0),
                                                 border_radius=2,
                                                 color_hover=QColor(0, 0, 0, 35),
                                                 color_background=QColor(245, 243, 247),
                                                 color_border=QColor(101, 60, 147),
                                                 item_spacing=2,
                                                 item_height=20,
                                                 )

        self.ui.comboBox_data_type.setParams(border_radius=5,
                                             font_color=QColor(0, 0, 0),
                                             background_color=QColor(245, 243, 247)
                                             )
        self.ui.comboBox_data_type.setFont(font)
        self.data_type = ["uint8", "int8", "uint16", "int16", "float", "uint32", "int32"]
        self.ui.comboBox_data_type.addItems(self.data_type)

        # LineEdit
        self.ui.lineEdit_data.setParams(anim_start_color=QColor(230, 230, 230),
                                        anim_finish_color=QColor(118, 76, 167),
                                        background_color=QColor(245, 243, 247),
                                        font_color=QColor(10, 10, 10))
        self.ui.lineEdit_data.setGeometry(QRect(50, 50, 200, 24))
        self.ui.lineEdit_data.setPlaceholderText("请输入文字")
        self.ui.lineEdit_data.setFont(font)

        self.verticalLayout.addWidget(self.main_widget)


class CardBoxWidget(CardBoxDeletable):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)

        # 添加按钮
        self.button_add = BaseHoveringButton(self)
        self.button_add.setFont(font)
        self.button_add.clicked.connect(self.onAddWidget)
        self.button_add.setFixedSize(QSize(23, 23))
        self.button_add.setParams(font_color=QColor(255, 255, 255),
                                  border_radius=5,
                                  background_color=QColor(123, 80, 172),
                                  hovering_color=QColor(103, 60, 152),
                                  border_color=QColor(0, 0, 0, 0),
                                  text_padding=(-3,0,0,0),
                                  text_flag=Qt.AlignCenter | Qt.AlignHCenter,
                                  )
        self.button_add.setText("+")
        self.addWidget2ToolBox(self.button_add)

    def getCardWidget(self) -> (QWidget, QPushButton):
        card = CardWidget(self)
        return card, card.delPushButton


if __name__ == '__main__':
    app = QApplication([])
    m = CardBoxWidget()
    m.show()
    app.exec()
