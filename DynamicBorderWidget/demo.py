import sys

from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from DynamicBorderWidget import DynamicBorderWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    window.setGeometry(0, 0, 400, 500)
    window.setStyleSheet("background-color:rgba(0,0,0,0);")

    font = QFont()
    font.setFamilies([u"Consolas"])
    font.setPointSize(100)

    frame = DynamicBorderWidget(window)
    frame.setGeometry(100, 100, 200, 300)
    frame.setParams(border_radius=15,
                    border_width=4,
                    color_1=QColor(153,0,51,255),
                    color_2=QColor(255,153,0,255),
                    font_color=QColor(255, 255, 255),
                    inside_background_color=QColor("#006633"),
                    )

    frame.setFont(font)
    frame.setText("3")

    window.show()
    sys.exit(app.exec())