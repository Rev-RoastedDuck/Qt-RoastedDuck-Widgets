from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import SimpleButton_1, SimpleButton_2, SimpleButton_3, SimpleButton_4, SimpleButton_5, SimpleButton_6, \
    RWavyButton, GlowButton

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(650, 400)
    w.setWindowTitle("rrd-widget")
    w.setStyleSheet("background: #ffffff;")

    font = QFont()
    font.setPointSize(13)

    btn_1 = SimpleButton_1(w)
    btn_1.setGeometry(QRect(150 + 20,  80, 120, 40))
    btn_1.setParams(
        text="Hold That",
        border_radius=5,
        full_color=QColor(108, 53, 222),
        font_anim_start_color=QColor(108, 53, 222),
        font_anim_finish_color=QColor("#ffffff"),
    )

    btn_1.setFont(font)
    btn_1.setText("BUTTON")

    btn_2 = SimpleButton_2(w)
    btn_2.setGeometry(QRect(150 + 30 + 20 + 140, 80, 120, 40))
    btn_2.setParams(text="Hold That",
                    border_radius=5,
                    full_color=QColor(108, 53, 222),
                    font_anim_start_color=QColor(108, 53, 222),
                    font_anim_finish_color=QColor("#ffffff"),
                    )
    btn_2.setFont(font)
    btn_2.setText("BUTTON")

    btn_3 = SimpleButton_3(w)
    btn_3.setGeometry(QRect(150 + 20, 60 + 80, 120, 40))
    btn_3.setParams(
        text="Hold That",
        border_radius=5,
        full_color=QColor(108, 53, 222),
        font_anim_start_color=QColor(108, 53, 222),
        font_anim_finish_color=QColor("#ffffff"),
    )

    btn_3.setFont(font)
    btn_3.setText("BUTTON")

    btn_4 = SimpleButton_4(w)
    btn_4.setGeometry(QRect(150 + 30 + 20 + 140, 60 + 80, 120, 40))
    btn_4.setParams(
        text="Hold That",
        border_radius=5,
        full_color=QColor(108, 53, 222),
        font_anim_start_color=QColor(108, 53, 222),
        font_anim_finish_color=QColor("#ffffff"),
    )
    btn_4.setFont(font)
    btn_4.setText("BUTTON")

    btn_5 = SimpleButton_5(w)
    btn_5.setGeometry(QRect(150 + 20, 120 + 80, 120, 40))
    btn_5.setParams(color=QColor("#ffffff"),
                    border_radius=5,
                    first_text="Hold that",
                    second_text="Succeed",
                    first_background_color=QColor(108, 53, 222),
                    second_background_color=QColor(36, 27, 53),
                    )
    btn_5.setFont(font)

    btn_6 = SimpleButton_6(w)
    btn_6.setGeometry(QRect(150 + 20 + 30 + 140, 120 + 80, 120, 40))
    btn_6.setParams(color=QColor("#ffffff"),
                    border_radius=5,
                    first_text="Hold that",
                    second_text="Succeed",
                    first_background_color=QColor(108, 53, 222),
                    second_background_color=QColor(36, 27, 53),
                    )
    btn_6.setFont(font)

    btn_7 = RWavyButton(w)
    btn_7.setGeometry(QRect(150 + 20, 80 + 120 + 60, 120, 40))
    btn_7.setParams(font_color=QColor(183, 148, 192),
                    full_color=QColor(108, 53, 222),
                    border_radius=5,
                    )
    btn_7.setFont(font)
    btn_7.setText("Hold That")

    btn_8 = GlowButton(w)
    btn_8.setGeometry(QRect(150 + 20 + 30 + 140, 60 + 120 + 80, 120, 50))
    btn_8.setParams(border_radius=10,
                    font_color=QColor(0, 0, 0))
    btn_8.setFont(font)
    btn_8.setText("Start Coding")

    w.show()
    app.exec()
