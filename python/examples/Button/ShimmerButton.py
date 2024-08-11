from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import ShimmerButton

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(1920, 1080)
    w.move(0, 0)
    w.setStyleSheet("background-color:#000000")

    shimmer_button = ShimmerButton(w)
    shimmer_button.setParams(shimmer_color_1=QColor("#f9ea49"),
                             shimmer_color_2=QColor("#8bd59a"),
                             shimmer_blur_radius=60,
                             timer_interval=2
                             )
    shimmer_button.setGeometry(QRect(550, 200, 500, 250))
    shimmer_button.setStyleSheet("""ShimmerButton{
                                        background-color: rgba(255, 255, 0,0);
                                        color:#ffffff;
                                        border-radius:90px;
                                        }
                                """
                                 )

    font = QFont()
    font.setPointSize(40)
    shimmer_button.setFont(font)
    shimmer_button.setText("BUTTON")

    w.show()
    app.exec()