from PySide6.QtWidgets import QPushButton
import PySide6.QtGui

class ClickedButton(QPushButton):
    """按钮被点击后会变色"""
    def __init__(self,parent=None):
        super(ClickedButton, self).__init__(parent)

    def mousePressEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        super(ClickedButton, self).mousePressEvent(e)
        self.setStyleSheet("QPushButton{\n"
                           "	border-radius:18px;\n"
                           "	background-color:rgba(204,51,51,200);\n"
                           "}\n")
    def mouseReleaseEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        super(ClickedButton, self).mouseReleaseEvent(e)
        self.setStyleSheet("QPushButton{\n"
                           "	border-radius:18px;\n"
                           "	background-color: rgba(0, 0, 0, 100);\n"
                           "}\n")