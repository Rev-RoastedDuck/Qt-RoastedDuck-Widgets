from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from SimpleButton_1 import SimpleButton_1
from SimpleButton_2 import SimpleButton_2
from SimpleButton_3 import SimpleButton_3
from SimpleButton_4 import SimpleButton_4

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800, 800)
    w.setStyleSheet("background: #000000;")

    font = QFont()
    font.setPointSize(13)

    btn_1 = SimpleButton_1(w)
    btn_1.setGeometry(QRect(200, 260, 140, 45))
    btn_1.setParams(full_color=QColor("#00A97F"), font_anim_finish_color=QColor("#ffffff"), timer_interval=8)
    btn_1.setStyleSheet("""SimpleButton_1{
                            border:1px solid #00A97F;
                       	    border-radius:5px;
                            color:#00A97F;
                            } 
                        """)

    btn_1.setFont(font)
    btn_1.setText("BUTTON")

    btn_2 = SimpleButton_2(w)
    btn_2.setGeometry(QRect(200, 340, 140, 45))
    btn_2.setParams(full_color=QColor("#00A97F"), font_anim_finish_color=QColor("#ffffff"), timer_interval=8)
    btn_2.setStyleSheet("""SimpleButton_2{
                            border:1px solid #00A97F;
                       	    border-radius:5px;
                            color:#00A97F;
                            } 
                        """)
    btn_2.setFont(font)
    btn_2.setText("BUTTON")

    btn_3 = SimpleButton_3(w)
    btn_3.setGeometry(QRect(400, 260, 140, 45))
    btn_3.setParams(full_color=QColor("#00A97F"), font_anim_finish_color=QColor("#ffffff"), timer_interval=8)
    btn_3.setStyleSheet("""SimpleButton_3{
                            border:1px solid #00A97F;
                       	    border-radius:5px;
                            color:#00A97F;
                            } 
                        """)

    btn_3.setFont(font)
    btn_3.setText("BUTTON")

    btn_4 = SimpleButton_4(w)
    btn_4.setGeometry(QRect(400, 340, 140, 45))
    btn_4.setParams(full_color=QColor("#00A97F"), font_anim_finish_color=QColor("#ffffff"), timer_interval=8)
    btn_4.setStyleSheet("""SimpleButton_4{
                            border:1px solid #00A97F;
                       	    border-radius:5px;
                            color:#00A97F;
                            } 
                        """)
    btn_4.setFont(font)
    btn_4.setText("BUTTON")

    w.show()
    app.exec()
