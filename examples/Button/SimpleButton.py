from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import SimpleButton_1, SimpleButton_2, SimpleButton_3, SimpleButton_4, SimpleButton_5, SimpleButton_6

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800, 800)
    w.setStyleSheet("background: #000000;")

    font = QFont()
    font.setPointSize(13)

    btn_1 = SimpleButton_1(w)
    btn_1.setGeometry(QRect(190, 280, 140, 45))
    btn_1.setParams(
        text="Hold That",
        border_radius=5,
        full_color=QColor("#00A97F"),
        font_anim_start_color=QColor("#00A97F"),
        font_anim_finish_color=QColor("#ffffff"),
    )

    btn_1.setFont(font)
    btn_1.setText("BUTTON")

    btn_2 = SimpleButton_2(w)
    btn_2.setGeometry(QRect(390, 280, 140, 45))
    btn_2.setParams(text="Hold That",
                    border_radius=5,
                    full_color=QColor("#00A97F"),
                    font_anim_start_color=QColor("#00A97F"),
                    font_anim_finish_color=QColor("#ffffff"),
                    )
    btn_2.setFont(font)
    btn_2.setText("BUTTON")

    btn_3 = SimpleButton_3(w)
    btn_3.setGeometry(QRect(190, 380, 140, 45))
    btn_3.setParams(
        text="Hold That",
        border_radius=5,
        full_color=QColor("#00A97F"),
        font_anim_start_color=QColor("#00A97F"),
        font_anim_finish_color=QColor("#ffffff"),
    )

    btn_3.setFont(font)
    btn_3.setText("BUTTON")

    btn_4 = SimpleButton_4(w)
    btn_4.setGeometry(QRect(390, 380, 140, 45))
    btn_4.setParams(
        text="Hold That",
        border_radius=10,
        full_color=QColor("#00A97F"),
        font_anim_start_color=QColor("#00A97F"),
        font_anim_finish_color=QColor("#ffffff"),
    )
    btn_4.setFont(font)
    btn_4.setText("BUTTON")

    btn_5 = SimpleButton_5(w)
    btn_5.setGeometry(QRect(190, 680, 140, 45))
    btn_5.setParams(color=QColor("#ffffff"),
                    border_radius=10,
                    first_text="Hold that",
                    second_text="Succeed",
                    first_background_color=QColor("#21dc62"),
                    second_background_color=QColor("#1e90ff"),
                    )
    btn_5.setFont(font)

    btn_6 = SimpleButton_6(w)
    btn_6.setGeometry(QRect(390, 680, 140, 45))
    btn_6.setParams(color=QColor("#ffffff"),
                    border_radius=10,
                    first_text="Hold that",
                    second_text="Succeed",
                    first_background_color=QColor("#21dc62"),
                    second_background_color=QColor("#1e90ff"),
                    )
    btn_6.setFont(font)

    w.show()
    app.exec()
