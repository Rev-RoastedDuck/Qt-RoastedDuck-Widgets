from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget


from rrd_widgets import GlowButton


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(650, 400)
    w.setWindowTitle("rrd-widget")
    w.setStyleSheet("background: #ffffff;")

    btn = GlowButton(w)
    btn.setGeometry(QRect(200, 120, 250, 80))
    btn.setParams(border_radius=16,
                  font_color=QColor(0,0,0))

    font = QFont()
    font.setPointSize(22)
    btn.setFont(font)
    btn.setText("Start Coding")

    w.show()
    app.exec()