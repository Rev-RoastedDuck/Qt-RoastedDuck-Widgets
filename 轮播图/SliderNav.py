import PySide6
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QButtonGroup, QHBoxLayout, QSizePolicy

class SliderNav(QWidget):
    """图片导航栏，鼠标悬浮导航栏的红点，会切换图片(通过发送信号实现)"""
    changePixmap_signal = Signal(int)
    changeColor_signal = Signal(int)

    def __init__(self, parent, button_num):
        super().__init__(parent)
        self.button_num = button_num
        self.button_size = 6

        self.ui()
        self.__signalConnect()
        self.__highlightButton()

    def ui(self):
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.button_group = QButtonGroup(self)
        layout = QHBoxLayout(self)
        layout.setSpacing(10)

        for id in range(self.button_num):
            button = HoveredButton(id)
            button.setFixedSize(self.button_size, self.button_size)
            button.hovered_signal.connect(self.buttonHoverEvent)
            button.setStyleSheet(
                f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(0,0,0,50);}}QPushButton:hover{{border-radius:{self.button_size // 2}px;background-color:rgba(255,0,0,255)}}")
            self.button_group.addButton(button, id)
            layout.addWidget(button)

    def __signalConnect(self):
        self.changeColor_signal.connect(self.changeColor)

    def buttonHoverEvent(self,id:int) -> None:
        self.changePixmap_signal.emit(id)

    def changeColor(self, button_id: int):
        for id in range(self.button_num):
            button = self.button_group.button(id)
            button.setStyleSheet(
                f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(0,0,0,50);}}")

        button = self.button_group.button(button_id)
        button.setStyleSheet(
            f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(255,0,0,255);}}")

    def __highlightButton(self):
        """m默认让中间的按钮高亮"""
        self.changeColor_signal.emit(1)

class HoveredButton(QPushButton):
    """鼠标悬浮，携带id，发送信号"""
    hovered_signal = Signal(int)

    def __init__(self, id:int) -> None:
        super(HoveredButton, self).__init__()
        self.id = id

    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None:
        self.hovered_signal.emit(self.id)