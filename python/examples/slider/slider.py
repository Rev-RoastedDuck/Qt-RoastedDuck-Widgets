from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import Silder

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(300, 300)

    s = Silder(Qt.Orientation.Vertical, w)
    s.resize(30, 200)
    s.move(5, 5)

    s2 = Silder(Qt.Orientation.Horizontal, w)
    s2.setGradient(start_color=QColor("#943b8e"),
                   midd_color=QColor("#ca3fa1"),
                   end_color=QColor(0, 89, 89))
    s2.setMinimum(10)
    s2.setMaximum(100)
    s2.resize(200, 30)
    s2.move(50, 5)
    w.show()
    app.exec()
