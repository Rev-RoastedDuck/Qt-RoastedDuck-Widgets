from PySide6.QtWidgets import QWidget,QLineEdit, QLabel
from PySide6.QtCore import QRect, QSize, Qt,QPropertyAnimation, QPoint, QAbstractAnimation, QParallelAnimationGroup

from getStyleProperty import get_property

class RInput_1(QWidget):
    def __init__(self, parent=None):
        super(RInput_1, self).__init__(parent)
        self.componentInit()
        self.is_focus = False

    def componentInit(self):
        self.placeholder = QLabel(self)
        self.editer = QLineEdit(self)
        self.editer.setFocusPolicy(Qt.ClickFocus)

    def setPos(self):
        self.editer.setGeometry(0,self.height()-self.editer_raw_h,self.width(),self.editer_raw_h)
        self.placeholder.setGeometry(10,self.height()-self.editer_raw_h-self.placeholder_raw_h,self.width(),self.placeholder_raw_h)

    def setParams(self,editer_height:int):
        self.editer_show_h = editer_height

    def setTextToPlaceholder(self, text: str):
        self.placeholder.setText(text)

    def setFontToEditer(self, font):
        self.editer.setFont(font)

    def setFontToPlaceholder(self, font):
        self.placeholder.setFont(font)

    def getStyleSheetParams(self):
        """ 提取样式 """
        RInput_property: dict = get_property(self)["RInput"]
        self.font_color = RInput_property["color"]
        self.border_radius = RInput_property["border-radius"]
        self.background_color = RInput_property["background-color"]

    def setStyleSheetToComponent(self):
        self.editer.setStyleSheet(f"background-color:{self.background_color};border-radius:{self.border_radius};color:{self.font_color};padding-left:10px;")
        self.placeholder.setStyleSheet(f"background-color:rgba(255,255,255,0);color:{self.background_color};padding-bottom:3px")

    def setStyleSheet(self, styleSheet):
        super(RInput_1, self).setStyleSheet(styleSheet)
        self.getStyleSheetParams()
        self.setStyleSheetToComponent()

    def animCreat(self):
        self.editer_anim = QPropertyAnimation()
        self.editer_anim.setTargetObject(self.editer)
        self.editer_anim.setPropertyName(b"geometry")
        self.editer_anim.setDuration(100)
        self.editer_anim.setStartValue(QRect(QPoint(self.editer_raw_show_x, self.editer_raw_y), QSize(self.editer_raw_show_w, self.editer_raw_h)))
        self.editer_anim.setEndValue(QRect(QPoint(self.editer_raw_show_x, self.editer_show_y), QSize(self.editer_raw_show_w, self.editer_show_h)))

        self.label_anim = QPropertyAnimation()
        self.label_anim.setTargetObject(self.placeholder)
        self.label_anim.setPropertyName(b"pos")
        self.label_anim.setDuration(100)
        self.label_anim.setStartValue(QPoint(self.placeholder_raw_x, self.placeholder_raw_y))
        self.label_anim.setEndValue(QPoint(self.placeholder_show_x, self.placeholder_show_y))

        self.animationGroup = QParallelAnimationGroup()
        self.animationGroup.addAnimation(self.editer_anim)
        self.animationGroup.addAnimation(self.label_anim)

    def animParamsConfig(self):
        """根据输入框的总高度，计算各个组件的高度"""
        self.editer_raw_h = 2
        self.editer_raw_show_x = 0
        self.editer_raw_show_w = self.width()

        self.editer_show_y = self.height() - self.editer_show_h
        self.editer_raw_y = self.height()-self.editer_raw_h

        self.placeholder_raw_x = 10
        self.placeholder_show_x = 2
        self.placeholder_raw_h = self.height() - self.editer_show_h

        self.placeholder_show_y = self.editer_show_y - self.placeholder_raw_h
        self.placeholder_raw_y = self.editer_raw_y - self.placeholder_raw_h

    def mousePressEvent(self, event):
        super(RInput_1, self).mousePressEvent(event)
        if not self.is_focus:
            self.is_focus = True
            self.editer.setFocus()
            self.animationGroup.setDirection(QAbstractAnimation.Forward)
            self.animationGroup.start()

    def leaveEvent(self,event):
        super(RInput_1, self).leaveEvent(event)
        if self.is_focus and not self.editer.text():
            self.is_focus = False
            self.editer.clearFocus()
            self.animationGroup.setDirection(QAbstractAnimation.Backward)
            self.animationGroup.start()

    def setGeometry(self, g):
        super(RInput_1, self).setGeometry(g)
        self.animParamsConfig()
        self.setPos()
        self.animCreat()




