from PySide6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, QPoint, QParallelAnimationGroup, QRect, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QScrollArea, QWidgetItem, QBoxLayout


class CardBoxBase(QWidget):
    def __init__(self, parent=None,orientation:Qt.Orientation=Qt.Horizontal):
        super().__init__(parent=parent)
        self.orientation = orientation
        self.__uiInit()

    def __uiInit(self):
        self.resize(550, 300)

        # 滚动区域
        self.scroll_layout = QHBoxLayout()

        if self.orientation == Qt.Horizontal:
            self.scroll_layout = QHBoxLayout()
        else:
            self.scroll_layout = QVBoxLayout()
            self.scroll_layout.setDirection(QBoxLayout.BottomToTop)

        self.scroll_layout.addStretch(1)
        self.scroll_layout.setContentsMargins(12, 0, 12, 9)



        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.scroll_widget)
        if self.orientation==Qt.Horizontal:
            self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        else:
            self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll.setStyleSheet("""
        /* QScrollArea */
        QScrollArea{
            border: 0px solid;
            border-right-width: 0px;
            border-right-color: #dcdbdc;
            background-color: rgba(255,255,255,0);
        }

        /* QScrollArea.viewport */
        QScrollArea QWidget{
            border: 0px solid;
            border-right-width: 0px;
            border-right-color: #dcdbdc;
            background-color: rgba(255,255,255,0);
        }

        /* QScrollBar */
        QScrollBar:horizontal {
            border: 0px solid;
            background: rgba(218, 206, 230);
            height: 12px;
            border-radius: 5px;
        }
        
        /* QScrollBar */
        QScrollBar:vertical {
            border: 0px solid;
            background: rgba(218, 206, 230);
            width: 12px;
            border-radius: 5px;
        }

        /* QScrollBar.handle */
        QScrollBar::handle:horizontal,QScrollBar::handle:vertical {
            background: rgb(103, 63, 150);
            min-height: 10px;
            border-radius: 5px;
            border: none;
        }

        /* QScrollBar.handle :a line that handle x/y to handle's height */
        QScrollBar::add-line:horizontal,QScrollBar::add-line:vertical {
            border: 0px solid grey;
            background: #32CC99;
            height: 0px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }

        /* QScrollBar.handle: a line that 0 to handle x/y */
        QScrollBar::sub-line:horizontal,QScrollBar::sub-line:vertical {
            border: 0px solid grey;
            background: #32CC99;
            height: 0px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }

        /* QScrollBar.page: area that 0 to handle x/y or handle x/y to handle's height */
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            width: 0px;
            height: 0px;
        }
        """)
        # self.scroll.viewport().setStyleSheet("""
        # *{
        #     border:none;
        #     background-color:transparent;
        # }
        # """)

        # 功能区域
        self.tool_box = QWidget(self)
        self.tool_box.setObjectName("tool_box")
        self.tool_box.setStyleSheet("""
            *{
                border:none;
                background-color:transparent;
            }
            #tool_box{
                 border-bottom: 2px solid rgba(154, 115, 181,150);
            }
        """)
        self.tool_box.setAttribute(Qt.WA_StyledBackground, True)
        self.tool_box_layout = QHBoxLayout(self.tool_box)
        self.tool_box_layout.addStretch(1)
        self.tool_box_layout.setSpacing(5)
        self.tool_box_layout.setContentsMargins(5, 0, 8, 5)

        # 整体布局
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(3)
        mainLayout.setContentsMargins(0, 8, 0, 8)
        mainLayout.addWidget(self.tool_box)
        mainLayout.addWidget(self.scroll)

    def addWidget2ToolBox(self,button:QPushButton,pos:int = 1):
        """
        添加按钮到工具栏
        :param button:按钮
        :param pos:   位置
        :return:
        """
        self.tool_box_layout.insertWidget(pos, button)

    def addWidget(self, card_widget=None,*args):
        """
        需要用一个按钮绑定该方法
        :param card_widget:
        :param button_del:
        :return:
        """
        self.scroll_layout.addWidget(card_widget)

        QTimer.singleShot(0, lambda: self.scroll_widget.adjustSize())  # 调整滚动区域大小
        # if self.orientation == Qt.Horizontal:
            # QTimer.singleShot(0, lambda: self.scroll.horizontalScrollBar().setValue(
            #     self.scroll.horizontalScrollBar().maximum()))  # 移动滑动条
        # else:
            # QTimer.singleShot(0, lambda: self.scroll.verticalScrollBar().setValue(
            #     self.scroll.verticalScrollBar().maximum()))  # 移动滑动条


class CardBoxDeletable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.trigger = None
        self.del_card:list = []
        self.is_anim_group_connected = False
        self.animationGroup = QParallelAnimationGroup()
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.__uiInit()

    def __uiInit(self):
        self.resize(550, 300)

        # 滚动区域
        self.scroll_layout = QHBoxLayout()
        # self.scroll_layout.addStretch(1)  暂定

        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.scroll_widget)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("""
        /* QScrollArea */
        QScrollArea{
            border: 0px solid;
            border-right-width: 0px;
            border-right-color: #dcdbdc;
            background-color: rgba(255,255,255,0);
        }
        
        /* QScrollArea.viewport */
        QScrollArea QWidget{
            border: 0px solid;
            border-right-width: 0px;
            border-right-color: #dcdbdc;
            background-color: rgba(255,255,255,0);
        }
        
        /* QScrollBar */
        QScrollBar:horizontal {
            border: 0px solid;
            background: rgba(218, 206, 230);
            height: 12px;
            border-radius: 5px;
        }
        
        /* QScrollBar.handle */
        QScrollBar::handle:horizontal {
            background: rgb(103, 63, 150);
            min-height: 10px;
            border-radius: 5px;
            border: none;
        }
        
        /* QScrollBar.handle :a line that handle x/y to handle's height */
        QScrollBar::add-line:horizontal {
            border: 0px solid grey;
            background: #32CC99;
            height: 0px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }
        
        /* QScrollBar.handle: a line that 0 to handle x/y */
        QScrollBar::sub-line:horizontal {
            border: 0px solid grey;
            background: #32CC99;
            height: 0px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
        
        /* QScrollBar.page: area that 0 to handle x/y or handle x/y to handle's height */
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
            width: 0px;
            height: 0px;
        }
        """)
        # self.scroll.viewport().setStyleSheet("""
        # *{
        #     border:none;
        #     background-color:transparent;
        # }
        # """)

        # 功能区域
        self.tool_box = QWidget(self)
        self.tool_box.setObjectName("tool_box")
        self.tool_box.setStyleSheet("""
            #tool_box{
                border:none;
                background-color:transparent;
            }
            #tool_box{
                 border-bottom: 2px solid rgba(154, 115, 181,150);
             }
        """)
        self.tool_box.setAttribute(Qt.WA_StyledBackground, True)
        self.tool_box_layout = QHBoxLayout(self.tool_box)
        self.tool_box_layout.addStretch(1)
        self.tool_box_layout.setSpacing(5)
        self.tool_box_layout.setContentsMargins(0, 0, 0, 8)


        # 整体布局
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.tool_box)
        mainLayout.addWidget(self.scroll)

    def getCardWidget(self) -> (QWidget, QPushButton):
        """
        继承的窗口，需要重写该函数
        QWidget:        卡片组件
        QPushButton:    删除卡片的按钮
        :return:
        """
        # card = CardWidget(self)
        # return card, card.delPushButton
        return QWidget(),QPushButton()

    def onAddWidget(self, card_widget=None, button_del=None):
        """
        需要用一个按钮绑定该方法
        :param card_widget:
        :param button_del:
        :return:
        """
        if card_widget is None and button_del is None:
            card_widget, button_del = self.getCardWidget()

        button_del.clicked.connect(self.onDelCard)
        self.scroll_layout.addWidget(card_widget)
        QTimer.singleShot(0, lambda: self.scroll_widget.adjustSize())  # 调整滚动区域大小
        QTimer.singleShot(0, lambda: self.scroll.horizontalScrollBar().setValue(
            self.scroll.horizontalScrollBar().maximum()))  # 移动滑动条

    def onDelCard(self):
        """
        提供外部按钮绑定，不可设置成私有方法
        :return:
        """
        self.trigger = self.sender()
        if isinstance(self.trigger, QPushButton):
            self.trigger = self.trigger.parent()

        self.animationGroup = QParallelAnimationGroup()  # 初始化

        # 卡片下移
        start_pos = self.trigger.pos()
        end_pos = QPoint(self.trigger.pos().x(), self.trigger.pos().y() + self.height())

        animation_moveY = QPropertyAnimation(self.trigger, b"pos")
        animation_moveY.setDuration(300)
        animation_moveY.setEndValue(end_pos)
        animation_moveY.setStartValue(start_pos)
        animation_moveY.setEasingCurve(QEasingCurve.OutQuad)
        self.animationGroup.addAnimation(animation_moveY)

        # 卡片左移
        start_index = self.scroll_layout.indexOf(self.trigger) + 1
        end_index = int(self.width() / self.trigger.width()) + 2

        for i in range(start_index, end_index):
            item = self.scroll_layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                widget = item.widget()
                if isinstance(widget, QWidget):
                    start_pos = widget.pos()
                    end_pos = QPoint(widget.pos().x() - widget.width(), widget.pos().y())

                    animation = QPropertyAnimation(widget, b"pos")
                    animation.setDuration(250)
                    animation.setEndValue(end_pos)
                    animation.setStartValue(start_pos)
                    animation.setEasingCurve(QEasingCurve.OutQuad)
                    self.animationGroup.addAnimation(animation)

        # if self.is_anim_group_connected:
        #     self.animationGroup.finished.disconnect()

        # result = self.animationGroup.finished.connect(self.__onAnimFinished)
        # self.is_anim_group_connected = True if result else False

        self.animationGroup.finished.connect(self.__onAnimFinished)

        self.animationGroup.start()

    def clearAllCard(self):
        self.animationGroup = QParallelAnimationGroup()  # 初始化
        for i in range(0,self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                widget = item.widget()
                if isinstance(widget, QWidget):
                    start_pos = widget.pos()
                    end_pos = QPoint(widget.pos().x(),widget.pos().y() + self.height())

                    self.del_card.append(widget)
                    animation_moveY = QPropertyAnimation(widget, b"pos")
                    animation_moveY.setDuration(300)
                    animation_moveY.setEndValue(end_pos)
                    animation_moveY.setStartValue(start_pos)
                    animation_moveY.setEasingCurve(QEasingCurve.OutQuad)
                    self.animationGroup.addAnimation(animation_moveY)

        # if self.is_anim_group_connected:
        #     self.animationGroup.finished.disconnect()

        # result = self.animationGroup.finished.connect(self.__onClearAllFinish)
        # self.is_anim_group_connected = True if result else False

        self.animationGroup.finished.connect(self.__onClearAllFinish)

        self.animationGroup.start()

    def __onAnimFinished(self):
        self.trigger.deleteLater()
        QTimer.singleShot(0, lambda: self.scroll_widget.adjustSize())

    def __onClearAllFinish(self):
        for i in range(0,self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                widget = item.widget()
                if isinstance(widget, QWidget):
                    widget.deleteLater()
        QTimer.singleShot(0, lambda: self.scroll_widget.adjustSize())

    def addWidget2ToolBox(self,button:QPushButton,pos:int = 1):
        """
        添加按钮到工具栏
        :param button:按钮
        :param pos:   位置
        :return:
        """
        self.tool_box_layout.insertWidget(pos, button)

