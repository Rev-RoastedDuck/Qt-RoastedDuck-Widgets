from PySide6.QtGui import QFont
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication,QWidget

from ExpInput import ExpInput

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background-color:#000000")

    font = QFont()
    font.setFamily("微软雅黑")


    input_1 = ExpInput(w)
    input_1.setParams(editer_height = 35)
    input_1.setStyleSheet("ExpInput{background-color:#45d2a2;border:5px;color:#ffffff;border-radius:10px}")
    input_1.setGeometry(QRect(300, 150, 180, 60))
    font.setPointSize(13)
    input_1.setFontToEditer(font)

    font.setPointSize(10)
    input_1.setFontToPlaceholder(font)
    input_1.setTextToPlaceholder("请输入内容")


    w.show()
    app.exec()