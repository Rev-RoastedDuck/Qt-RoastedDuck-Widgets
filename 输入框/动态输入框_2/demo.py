import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication,QWidget

from RInput_2 import RInput_2_1,RInput_2_2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1900,800)
    w.setStyleSheet("background-color:#000000")

    font = QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(10)

    a = RInput_2_2(w)
    a.setStyleSheet("RInput_2_2{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a.setGeometry(600,300,200,35)
    a.setPlaceholderText("请输入文字")
    a.setFont(font)

    a_1 = RInput_2_2(w)
    a_1.setStyleSheet("RInput_2_2{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_1.setGeometry(600,340,200,35)
    a_1.setPlaceholderText("请输入文字")
    a_1.setFont(font)

    a_2 = RInput_2_1(w)
    a_2.setStyleSheet("RInput_2_1{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_2.setGeometry(600,380,200,35)
    a_2.setPlaceholderText("请输入文字")
    a_2.setFont(font)

    a_3 = RInput_2_1(w)
    a_3.setStyleSheet("RInput_2_1{background-color:rgba(255,255,255,0);border-radius:10px;padding-left:10px;color:#ffffff;}")
    a_3.setGeometry(600,420,200,35)
    a_3.setPlaceholderText("请输入文字")
    a_3.setFont(font)



    w.show()
    app.exec()