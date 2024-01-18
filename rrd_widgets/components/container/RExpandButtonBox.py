"""
Qt-RoastedDuck-Widgets
======================
Qt widgets-based implementation of the Material Design specification.

Repository at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.

Demo are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/Demo.

Examples are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/examples.

Information:
    WeChat: Roast_71.
    csdnBlog: https://blog.csdn.net/m0_72760466?type=blog.

:copyright: (c) 2023 by Rev-RoastedDuck.
:license: GPLv3, see LICENSE for more details.
"""

from PySide6.QtCore import QEasingCurve, QPoint, QAbstractAnimation
from PySide6.QtCore import (QRect,
                            QSize, QPropertyAnimation, QTimer)
from PySide6.QtWidgets import (QFrame, QPushButton)

from ...common.icon.binary_data_icon import icon_rexpand_button_box as icon


from rrd_widgets.components.layout.RGridLayout import RGridLayout


class RButton(QFrame):
    def __init__(self, size,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fixSize = size
        self.ui()

    def ui(self):
        self.setMaximumSize(self.fixSize)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(QPoint(0,0),self.fixSize))
        self.pushButton.setMaximumSize(self.fixSize)
        self.setStyleSheet("QPushButton{background-color:rgba(255,255,255,0)}")

class RExpandButtonBox(QFrame):
    def __init__(self,parent):
        super(RExpandButtonBox, self).__init__(parent=parent)
        self.paramsInit()
        self.widgetInit()

    def widgetInit(self):
        self.pushButton_NW = RButton(QSize())
        self.pushButton_SE = RButton(QSize())
        self.pushButton_W = RButton(QSize())
        self.pushButton_SW = RButton(QSize())
        self.pushButton_N = RButton(QSize())
        self.pushButton_NE = RButton(QSize())
        self.pushButton_E = RButton(QSize())
        self.pushButton_Center = RButton(QSize())
        self.pushButton_S = RButton(QSize())



    def paramsInit(self):
        self.locatorBoxSize: QSize = QSize()  # 定位Frame的尺寸
        self.locatorBoxWidgetWidth:int = 0 # 定位按钮的宽度
        self.locatorBoxWidgetSpacing:int = 0 # 定位按钮间的间隔

        self.expandBoxWidgetSize: QSize = QSize()  # 伸缩组件的尺寸
        self.expandBoxWidgetWidth:int = 0 # 伸缩组件内按钮的宽度
        self.expandBoxWidgetSpacing:int = 0 # 伸缩组件内按钮的间隔

        self.animationDuration:int = 0 # 每个按钮的动画的时间
        self.timeOffset = 50 # 动画间隔

        self.widgetList = []

    def addWidget(self,w):
        self.widgetList.append(w)
        if len(self.widgetList) == 9:
            self.setConfig()

    def setConfig(self):
        (self.pushButton_E, self.pushButton_W, self.pushButton_N,
         self.pushButton_S, self.pushButton_Center, self.pushButton_NW,
         self.pushButton_SE, self.pushButton_NE, self.pushButton_SW) = self.widgetList[:9]
        self.ui() # 不可以放在paintEvent，showEvent中调用
        QTimer.singleShot(0, lambda: self.animationParams())

    def ui(self):
        self.setObjectName(u"frameContainer")
        self.setFixedSize(self.expandBoxWidgetSize)
        self.frame_3 = QFrame(self)
        self.frame_3.setFixedSize(self.locatorBoxSize)
        self.frame_3.move((self.width() - self.frame_3.width()) // 2, (self.height() - self.frame_3.height()) // 2)
        self.frame_3.setStyleSheet(u"QFrame,QPushButton{"
                                   "	background-color: rgba(255, 0, 0,0);"
                                   "}")
        self.pushButton_n = QPushButton(self.frame_3)
        self.pushButton_n.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_sw = QPushButton(self.frame_3)
        self.pushButton_sw.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_se = QPushButton(self.frame_3)
        self.pushButton_se.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_s = QPushButton(self.frame_3)
        self.pushButton_s.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_w = QPushButton(self.frame_3)
        self.pushButton_w.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_c = QPushButton(self.frame_3)
        self.pushButton_c.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_nw = QPushButton(self.frame_3)
        self.pushButton_nw.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_e = QPushButton(self.frame_3)
        self.pushButton_e.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.pushButton_ne = QPushButton(self.frame_3)
        self.pushButton_ne.setFixedSize(QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth))

        self.buttonBox_mini = RGridLayout(self.frame_3, self.locatorBoxSize)
        self.buttonBox_mini.setGeometry(0, 0, 0, 0)
        self.buttonBox_mini.grid_width = self.locatorBoxWidgetWidth
        self.buttonBox_mini.grid_height = self.locatorBoxWidgetWidth
        self.buttonBox_mini.spacing = self.locatorBoxWidgetSpacing
        self.buttonBox_mini.addWidget(self.pushButton_nw, 0, 0)
        self.buttonBox_mini.addWidget(self.pushButton_n, 0, 1)
        self.buttonBox_mini.addWidget(self.pushButton_ne, 0, 2)
        self.buttonBox_mini.addWidget(self.pushButton_w, 1, 0)
        self.buttonBox_mini.addWidget(self.pushButton_c, 1, 1)
        self.buttonBox_mini.addWidget(self.pushButton_e, 1, 2)
        self.buttonBox_mini.addWidget(self.pushButton_sw, 2, 0)
        self.buttonBox_mini.addWidget(self.pushButton_s, 2, 1)
        self.buttonBox_mini.addWidget(self.pushButton_se, 2, 2)
        self.buttonBox_mini.setStyleSheet("#RButtonBox{"
                                          "	background-color: rgba(250, 0, 250,0);\n"
                                          "}")


        self.frame = QFrame(self)
        self.frame.setObjectName(u"frameExpandBox")
        self.frame.setGeometry(QRect(QPoint(0, 0),self.expandBoxWidgetSize))


        self.buttonBox = RGridLayout(self, self.expandBoxWidgetSize)
        self.buttonBox.setGeometry(0, 0, 0, 0)
        self.buttonBox.grid_width = self.expandBoxWidgetWidth
        self.buttonBox.grid_height = self.expandBoxWidgetWidth
        self.buttonBox.spacing = self.expandBoxWidgetSpacing
        self.buttonBox.addWidget(self.pushButton_NW, 0, 0)
        self.buttonBox.addWidget(self.pushButton_N, 0, 1)
        self.buttonBox.addWidget(self.pushButton_NE, 0, 2)
        self.buttonBox.addWidget(self.pushButton_W, 1, 0)
        self.buttonBox.addWidget(self.pushButton_Center, 1, 1)
        self.buttonBox.addWidget(self.pushButton_E, 1, 2)
        self.buttonBox.addWidget(self.pushButton_SW, 2, 0)
        self.buttonBox.addWidget(self.pushButton_S, 2, 1)
        self.buttonBox.addWidget(self.pushButton_SE, 2, 2)
        self.buttonBox.setStyleSheet("#RButtonBox{"
                        "	background-color: rgba(255, 0, 255,0);\n"
                        "}"
                        )

    def animationParams(self):
        '''
        动画参数配置
        :return:
        '''
        # 正向动画半径结束值
        self.forwardRadius = self.locatorBoxWidgetWidth // 2
        # 正向动画颜色结束值
        self.forwardColor = "rgba(255, 255, 255,255)"
        # 正向动画结束 按钮尺寸值
        self.forwardSize_RButton = QSize(self.locatorBoxWidgetWidth, self.locatorBoxWidgetWidth)

        # 反向动画半径结束值
        self.backwardRadius = self.expandBoxWidgetWidth // 2
        # 反向动画颜色结束值
        self.backwardColor = "rgba(51, 56, 73,255)"
        # 反向动画结束 按钮尺寸值
        self.backwardSize = QSize(self.expandBoxWidgetWidth, self.expandBoxWidgetWidth)

        # 判断展开/伸缩
        self.is_fold = 0

        self.timer = QTimer()
        self.timer.setInterval(self.timeOffset)
        self.timer.timeout.connect(self.animationForward_start)

        self.animationPreStartList = [self.animationForward_pre, self.animationBackward_pre]
        self.animationInit()
        self.animationList = [self.animationE,self.animationW,self.animationN,self.animationS,self.animationCenter,self.animationNW,self.animationSE,self.animationNE,self.animationSW,self.animationFrame]
        self.animationList_index = 0

    def mouseReleaseEvent(self, event):
        super(RExpandButtonBox, self).mousePressEvent(event)
        self.animationPreStartList[self.is_fold]()
        self.timer.start()

    def animationInit(self):

        self.animationE = QPropertyAnimation(self.pushButton_E, b"geometry")
        self.animationE.setEasingCurve(QEasingCurve.OutQuad)
        self.animationE.setDuration(self.animationDuration)
        self.animationE.setStartValue(self.pushButton_E.geometry())
        self.animationE.setEndValue(self.getEndValue(self.pushButton_e.pos()))
        self.animationE.valueChanged.connect(lambda value: self.pushButton_E.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationW = QPropertyAnimation(self.pushButton_W, b"geometry")
        self.animationW.setEasingCurve(QEasingCurve.OutQuad)
        self.animationW.setDuration(self.animationDuration)
        self.animationW.setStartValue(self.pushButton_W.geometry())
        self.animationW.setEndValue(self.getEndValue(self.pushButton_w.pos()))
        self.animationW.valueChanged.connect(lambda value: self.pushButton_W.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationS = QPropertyAnimation(self.pushButton_S, b"geometry")
        self.animationS.setEasingCurve(QEasingCurve.OutQuad)
        self.animationS.setDuration(self.animationDuration)
        self.animationS.setStartValue(self.pushButton_S.geometry())
        self.animationS.setEndValue(self.getEndValue(self.pushButton_s.pos()))
        self.animationS.valueChanged.connect(lambda value: self.pushButton_S.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationN = QPropertyAnimation(self.pushButton_N, b"geometry")
        self.animationN.setEasingCurve(QEasingCurve.OutQuad)
        self.animationN.setDuration(self.animationDuration)
        self.animationN.setStartValue(self.pushButton_N.geometry())
        self.animationN.setEndValue(self.getEndValue(self.pushButton_n.pos()))
        self.animationN.valueChanged.connect(lambda value: self.pushButton_N.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationNW = QPropertyAnimation(self.pushButton_NW, b"geometry")
        self.animationNW.setEasingCurve(QEasingCurve.OutQuad)
        self.animationNW.setDuration(self.animationDuration)
        self.animationNW.setStartValue(self.pushButton_NW.geometry())
        self.animationNW.setEndValue(self.getEndValue(self.pushButton_nw.pos()))
        self.animationNW.valueChanged.connect(lambda value: self.pushButton_NW.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationSE = QPropertyAnimation(self.pushButton_SE, b"geometry")
        self.animationSE.setEasingCurve(QEasingCurve.OutQuad)
        self.animationSE.setDuration(self.animationDuration)
        self.animationSE.setStartValue(self.pushButton_SE.geometry())
        self.animationSE.setEndValue(self.getEndValue(self.pushButton_se.pos()))
        self.animationSE.valueChanged.connect(lambda value: self.pushButton_SE.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationNE = QPropertyAnimation(self.pushButton_NE, b"geometry")
        self.animationNE.setEasingCurve(QEasingCurve.OutQuad)
        self.animationNE.setDuration(self.animationDuration)
        self.animationNE.setStartValue(self.pushButton_NE.geometry())
        self.animationNE.setEndValue(self.getEndValue(self.pushButton_ne.pos()))
        self.animationNE.valueChanged.connect(lambda value: self.pushButton_NE.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationSW = QPropertyAnimation(self.pushButton_SW, b"geometry")
        self.animationSW.setEasingCurve(QEasingCurve.OutQuad)
        self.animationSW.setDuration(self.animationDuration)
        self.animationSW.setStartValue(self.pushButton_SW.geometry())
        self.animationSW.setEndValue(self.getEndValue(self.pushButton_sw.pos()))
        self.animationSW.valueChanged.connect(lambda value: self.pushButton_SW.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))

        self.animationCenter = QPropertyAnimation(self.pushButton_Center,b"geometry")
        self.animationCenter.setEasingCurve(QEasingCurve.OutQuad)
        self.animationCenter.setDuration(self.animationDuration)
        self.animationCenter.setStartValue(self.pushButton_Center.geometry())
        self.animationCenter.setEndValue(self.getEndValue(self.pushButton_c.pos()))
        self.animationCenter.valueChanged.connect(lambda value: self.pushButton_Center.setStyleSheet(
            f"border-radius: {value.width() // 2-1}px;"
        ))


        self.animationFrame = QPropertyAnimation(self.frame,b"geometry")
        self.animationFrame.setEasingCurve(QEasingCurve.OutQuad)
        self.animationFrame.setDuration(self.animationDuration)
        self.animationFrame.setStartValue(self.frame.geometry())
        self.animationFrame.setEndValue(self.frame_3.geometry())

    def animationForward_pre(self):
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.animationForward_start)
        for button in self.findChildren(RButton):
            if button.objectName() == "pushButton_c":
                continue
            button.pushButton.hide()

    def animationForward_start(self):
        self.animationList[self.animationList_index].setDirection(QAbstractAnimation.Forward)
        targetObject = self.animationList[self.animationList_index].targetObject()
        if not targetObject.objectName() == "frame":
            self.animationList[self.animationList_index].finished.connect(
                lambda: self.animationForward_finished(targetObject)
            )

        self.animationList[self.animationList_index].start()
        self.animationList_index += 1
        if self.animationList_index > len(self.animationList)-1:
            self.animationList_index = len(self.animationList)-1
            self.is_fold ^= 1
            self.timer.stop()

    def animationForward_finished(self, pushButton):
        if isinstance(pushButton,RButton):
            pushButton.setStyleSheet(
                f"background-color: {self.forwardColor};"
                f"border-radius: {self.forwardRadius}px;"
            )
            pushButton.pushButton.setGeometry(QRect(QPoint(0, 0),QSize(0,0)))
            pushButton.update()

    def animationBackward_pre(self):
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.animationBackward_start)

    def animationBackward_start(self):
        self.animationList[self.animationList_index].setDirection(QAbstractAnimation.Backward)
        targetObject = self.animationList[self.animationList_index].targetObject()
        if not targetObject.objectName() == "frame":
            self.animationList[self.animationList_index].finished.disconnect()
            self.animationList[self.animationList_index].finished.connect(
                lambda: self.animationBackward_finished(targetObject))

        self.animationList[self.animationList_index].start()
        self.animationList_index -= 1
        if self.animationList_index < 0:
            self.animationList_index = 0
            self.is_fold ^= 1
            self.timer.stop()

    def animationBackward_finished(self, pushButton):
        if isinstance(pushButton,RButton):
            pushButton.setStyleSheet(
                 f"background-color: {self.backwardColor};"
                 f"border-radius: {self.backwardRadius}px;"
            )

            pushButton.pushButton.setGeometry(QRect(QPoint(0,0),self.backwardSize))
            pushButton.pushButton.show()
            pushButton.update()

    def getEndValue(self,pos):
        offset_x = self.buttonBox_mini.paddingH - self.buttonBox.paddingH
        offset_y = self.buttonBox_mini.paddingV - self.buttonBox.paddingV

        return QRect(self.frame_3.pos()+pos+QPoint(offset_x,offset_y),self.forwardSize_RButton)
