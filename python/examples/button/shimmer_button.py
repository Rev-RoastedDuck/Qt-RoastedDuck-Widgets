from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import ShimmerButton

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(650, 400)
    w.setWindowTitle("rrd-widget")
    w.setStyleSheet("background: #ffffff;")

    shimmer_button = ShimmerButton(w)
    shimmer_button.setParams(shimmer_color_1=QColor("#6f469f"),
                             shimmer_color_2=QColor("#784ea9"),
                             shimmer_blur_radius=30,
                             timer_interval=2
                             )
    shimmer_button.setGeometry(QRect(200, 120, 250, 125))
    shimmer_button.setStyleSheet("""ShimmerButton{
                                        background-color: rgba(255, 255, 0,0);
                                        color:#ffffff;
                                        border-radius:20px;
                                        }
                                """
                                 )

    font = QFont()
    font.setPointSize(18)
    shimmer_button.setFont(font)
    shimmer_button.setText("Start Coding")

    w.show()
    app.exec()