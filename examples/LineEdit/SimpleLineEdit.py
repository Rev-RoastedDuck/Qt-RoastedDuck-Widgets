import sys
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QApplication,QWidget

from rrd_widgets import SimpleLineEdit_1,SimpleLineEdit_2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 400)
    w.setStyleSheet("background-color:#ffffff")

    font = QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(10)

    a = SimpleLineEdit_1(w)
    a.setParams(anim_start_color=QColor(230,230,230),
                anim_finish_color=QColor(0, 89, 89),
                font_color=QColor(10,10,10))
    a.setGeometry(50, 50, 200, 35)
    a.setPlaceholderText("请输入文字")
    a.setFont(font)


    a_2 = SimpleLineEdit_2(w)
    a_2.setParams(anim_start_color=QColor(230,230,230),
                  anim_finish_color=QColor(0, 89, 89),
                  font_color=QColor(10,10,10))
    a_2.setGeometry(50, 120, 200, 35)
    a_2.setPlaceholderText("请输入文字")
    a_2.setFont(font)

    w.show()
    app.exec()