from PySide6.QtGui import QFont
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import ExpandLineEdit

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(650, 400)
    w.setWindowTitle("rrd-widget")
    w.setStyleSheet("background: #ffffff;")

    font = QFont()
    font.setFamily("微软雅黑")

    editer_data = ExpandLineEdit(w)
    editer_data.setFixedWidth(180)
    editer_data.setMinimumHeight(42)
    editer_data.setParams(editer_height=35)
    editer_data.setStyleSheet(
        "ExpInput{background-color:rgb(102, 62, 149);border:5px;color:rgb(255,255,255);border-radius:5px}")
    editer_data.setGeometry(QRect(240, 120, 180, 60))
    font.setPointSize(10)
    editer_data.setFontToEditer(font)

    font.setPointSize(10)
    editer_data.setFontToPlaceholder(font)
    editer_data.setPlaceholderText("请输入内容")

    w.show()
    app.exec()
