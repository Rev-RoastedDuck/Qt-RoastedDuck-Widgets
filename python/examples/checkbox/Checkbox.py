from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import CheckboxWidget

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("rrd-widget")
    window.setStyleSheet("background: #ffffff;")
    window.resize(300, 300)

    font = QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)

    c = CheckboxWidget(window)
    c.setParams(border_radius=5,background_color=QColor(255,255,255))
    c.resize(150, 30)
    c.move(70, 100-20)
    c.setFont(font)
    c.setText("你喜欢篮球🏀吗?")

    c1 = CheckboxWidget(window)
    c1.resize(150, 30)
    c1.move(70, 135-20)
    c1.setFont(font)
    c1.setText("你喜欢唱歌🎤吗?")

    c2 = CheckboxWidget(window)
    c2.resize(150, 30)
    c2.move(70, 170-20)
    c2.setFont(font)
    c2.setText("你喜欢跳舞💞吗?")

    c3 = CheckboxWidget(window)
    c3.resize(150, 30)
    c3.move(70, 205-20)
    c3.setFont(font)
    c3.setText("你喜欢Rap🎶吗?")




    window.show()

    app.exec()
