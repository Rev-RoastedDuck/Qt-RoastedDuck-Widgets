from PySide6.QtCore import QRect
from PySide6.QtGui import  QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget

from rrd_widgets import RWavyButton

if __name__ == '__main__':
    app = QApplication()
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background: #000000;")

    # 按钮样式配置
    btn = RWavyButton(w)
    btn.setGeometry(QRect(290, 280, 140, 45))
    btn.setParams(font_color=QColor("#ffffff"),
                  full_color=QColor(255, 89, 0),
                  border_radius=10,
                  )
    # 设置字体
    font = QFont()
    font.setPointSize(13)
    btn.setFont(font)
    btn.setText("Hold That")

    w.show()
    app.exec()