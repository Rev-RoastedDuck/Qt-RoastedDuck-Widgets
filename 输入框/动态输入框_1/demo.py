from PySide6.QtGui import QFont
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication,QWidget

from RInput import RInput

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(1920,800)
    w.setStyleSheet("background-color:#000000")

    font = QFont()
    font.setFamily("微软雅黑")


    r_input_1 = RInput(w)
    r_input_1.setParams(editer_height = 35)
    r_input_1.setStyleSheet("RInput{background-color:#45d2a2;border:5px;color:#ffffff;border-radius:10px}")
    r_input_1.setGeometry(QRect(500, 150, 180, 60))
    font.setPointSize(13)
    r_input_1.setFontToEditer(font)

    font.setPointSize(10)
    r_input_1.setFontToPlaceholder(font)
    r_input_1.setTextToPlaceholder("请输入内容")



    r_input_2 = RInput(w)
    r_input_2.setParams(editer_height = 40)
    r_input_2.setStyleSheet("RInput{background-color:#99CC00;border:5px;color:#ffffff;border-radius:10px}")
    r_input_2.setGeometry(QRect(500, 230, 230, 65))
    font.setPointSize(14)
    r_input_2.setFontToEditer(font)

    font.setPointSize(12)
    r_input_2.setFontToPlaceholder(font)
    r_input_2.setTextToPlaceholder("请输入内容")



    r_input_3 = RInput(w)
    r_input_3.setParams(editer_height = 40)
    r_input_3.setStyleSheet("RInput{background-color:#FF9900;border:5px;color:#ffffff;border-radius:10px}")
    r_input_3.setGeometry(QRect(500, 310, 280, 65))
    font.setPointSize(15)
    r_input_3.setFontToEditer(font)

    font.setPointSize(13)
    r_input_3.setFontToPlaceholder(font)
    r_input_3.setTextToPlaceholder("请输入内容")



    r_input_4 = RInput(w)
    r_input_4.setParams(editer_height = 45)
    r_input_4.setStyleSheet("RInput{background-color:#993333;border:5px;color:#ffffff;border-radius:10px}")
    r_input_4.setGeometry(QRect(500, 390, 330, 70))
    font.setPointSize(16)
    r_input_4.setFontToEditer(font)

    font.setPointSize(15)
    r_input_4.setFontToPlaceholder(font)
    r_input_4.setTextToPlaceholder("请输入内容")


    w.show()
    app.exec()