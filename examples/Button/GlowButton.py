from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget


from rrd_widgets import GlowButton


if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.setStyleSheet("background-color:#000000")

    btn = GlowButton(w)
    btn.move(50, 100)
    btn.resize(300, 100)
    btn.setParams(10, 5, QColor(255, 255, 255))

    font = QFont()
    font.setPointSize(25)
    btn.setFont(font)
    btn.setText("Start Coding")

    w.show()
    app.exec()