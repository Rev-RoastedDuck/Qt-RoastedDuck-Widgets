import sys

from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets.components.widget.ComboBox import ComboBoxWidget

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.resize(300, 300)

    font = QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)

    c = ComboBoxWidget(window)
    c.setFont(font)
    c.setItemHeight(28)
    c.setGeometry(80, 80, 160, 30)
    c.addItems(["篮球🏀", "唱歌🎤", "跳舞💞", "Rap🎶"])

    c.setItemParams(color_font=QColor(0, 0, 0),
                    border_radius=5,
                    color_hover=QColor(0, 0, 0, 35),
                    color_background=QColor(255, 255, 255),
                    color_border=QColor(0, 129, 140),
                    item_spacing=4,
                    item_height=28,
                    )

    c.setParams(border_radius=5,
                background_color=QColor(255, 255, 255)
                )

    window.show()

    sys.exit(app.exec())
