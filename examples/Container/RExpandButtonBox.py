"""
Qt-RoastedDuck-Widgets
======================
Qt widgets-based implementation of the Material Design specification.

Repository at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.

:copyright: (c) 2023 by Rev-RoastedDuck.
:license: GPLv3, see LICENSE for more details.
"""
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication,QWidget

from rrd_widgets import RButton, RExpandButtonBox

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.setStyleSheet("QWidget{background-color:rgba(0,0,0,255);}")
    w.resize(400,400)

    sizeRButton = QSize(50,50)
    iconRButton = QSize(20, 20)

    # 添加按钮
    if True:
        pushButton_NW = RButton(sizeRButton)
        icon_NW = QIcon()
        icon_NW.addFile(u":/icon/\u56fe\u6807/\u9f7f\u8f6e_cogwheel23.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_NW.pushButton.setIcon(icon_NW)
        pushButton_NW.pushButton.setIconSize(iconRButton)

        pushButton_SE = RButton(sizeRButton)
        icon_SE = QIcon()
        icon_SE.addFile(u":/icon/\u56fe\u6807/\u5587\u53ed.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_SE.pushButton.setIcon(icon_SE)
        pushButton_SE.pushButton.setIconSize(iconRButton)

        pushButton_W = RButton(sizeRButton)
        icon_W = QIcon()
        icon_W.addFile(u":/icon/\u56fe\u6807/\u5f55\u50cf.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_W.pushButton.setIcon(icon_W)
        pushButton_W.pushButton.setIconSize(iconRButton)

        pushButton_SW = RButton(sizeRButton)
        icon_SW = QIcon()
        icon_SW.addFile(u":/icon/\u56fe\u6807/\u7ef4\u4fee.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_SW.pushButton.setIcon(icon_SW)
        pushButton_SW.pushButton.setIconSize(iconRButton)

        pushButton_N = RButton(sizeRButton)
        icon_SW = QIcon()
        icon_SW.addFile(u":/icon/\u56fe\u6807/\u8054\u7cfb\u4eba.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_N.pushButton.setIcon(icon_SW)
        pushButton_N.pushButton.setIconSize(iconRButton)

        pushButton_NE = RButton(sizeRButton)
        iconNE = QIcon()
        iconNE.addFile(u":/icon/\u56fe\u6807/\u6e38\u620f\uff0c\u6e38\u620f\u673a.png", QSize(), QIcon.Normal,
                       QIcon.Off)
        pushButton_NE.pushButton.setIcon(iconNE)
        pushButton_NE.pushButton.setIconSize(iconRButton)

        pushButton_E = RButton(sizeRButton)
        icon_E = QIcon()
        icon_E.addFile(u":/icon/\u56fe\u6807/\u4fdd\u5b58.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_E.pushButton.setIcon(icon_E)
        pushButton_E.pushButton.setIconSize(iconRButton)

        pushButton_Center = RButton(sizeRButton)
        icon5_Center = QIcon()
        icon5_Center.addFile(u":/icon/\u56fe\u6807/\u5783\u573e\u6876 (2).png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_Center.pushButton.setIcon(icon5_Center)
        pushButton_Center.pushButton.setIconSize(iconRButton)

        pushButton_S = RButton(sizeRButton)
        icon_S = QIcon()
        icon_S.addFile(u":/icon/\u56fe\u6807/408\u6761\u5f62\u56fe-\u7ebf\u6027.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_S.pushButton.setIcon(icon_S)
        pushButton_S.pushButton.setIconSize(iconRButton)

    m = RExpandButtonBox(w)
    m.move(80,80)

    m.locatorBoxWidgetWidth = 8
    m.locatorBoxSize = QSize(80, 80)
    m.locatorBoxWidgetSpacing = 8

    m.expandBoxWidgetWidth = sizeRButton.width()
    m.expandBoxWidgetSize = QSize(250, 250)
    m.expandBoxWidgetSpacing = 20

    m.animationDuration = 250

    # 添加组件到RExpandBox
    m.addWidget(pushButton_W)
    m.addWidget(pushButton_E)
    m.addWidget(pushButton_N)
    m.addWidget(pushButton_S)
    m.addWidget(pushButton_Center)
    m.addWidget(pushButton_NE)
    m.addWidget(pushButton_SW)
    m.addWidget(pushButton_NW)
    m.addWidget(pushButton_SE)

    # 修改样式
    m.setStyleSheet(u"#frameExpandBox{"
                       "	background-color: rgb(33, 37, 50);"  # 伸缩Frame的背景颜色
                       "	border-radius:15px;"  # 伸缩Frame的圆角大小
                       "}"
                       "#frameContainer{"
                       "	background-color: rgba(255, 255, 255,0);"
                       "	border-radius:15px;"  # 容器Frame的圆角大小
                       "}"
                       "#frameContainer RButton { "
                       f"	border-radius: {sizeRButton.width()//2}px;"  # 按钮的圆角大小
                       "	background-color: rgba(51, 56, 73,255);"  # 按钮的背景颜色
                       "}"
                       "")


    w.show()
    app.exec()
