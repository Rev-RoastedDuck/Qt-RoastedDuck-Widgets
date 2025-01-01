from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
from rrd_widgets import TipsWidget, TipsStatus, CheckboxWidget


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("window")
        self.setWindowTitle("rrd-widget")

        self.resize(650,400)
        self.setStyleSheet("#window{"
                           "background-color:rgb(255,255,255);}"
                           ""
                           ""
                           "")

        font = QFont()
        font.setPointSize(11)

        s_btn = QPushButton(self)
        w_btn = QPushButton(self)
        d_btn = QPushButton(self)

        s_btn.clicked.connect(self.onSucceed)
        w_btn.clicked.connect(self.onWarning)
        d_btn.clicked.connect(self.onDangerous)

        s_btn.setGeometry(10+160,190+40,100,35)
        w_btn.setGeometry(120+160,190+40,100,35)
        d_btn.setGeometry(230+160,190+40,100,35)

        s_btn.setStyleSheet("QPushButton{"
                           "background-color:rgb(0, 129, 140);"
                           "color:#ffffff;"
                           "border-radius:5px;"
                           ""
                           "}")
        w_btn.setStyleSheet("QPushButton{"
                           "background-color:rgb(128, 110, 17);"
                           "color:#ffffff;"
                           "border-radius:5px;"
                           ""
                           "}")
        d_btn.setStyleSheet("QPushButton{"
                           "background-color:rgb(204, 51, 51);"
                           "color:#ffffff;"
                           "border-radius:5px;"
                           ""
                           "}")

        s_btn.setText("Succeed")
        d_btn.setText("Dangerous")
        w_btn.setText("Warning")

        s_btn.setFont(font)
        d_btn.setFont(font)
        w_btn.setFont(font)

        c = CheckboxWidget(self)
        c.setParams(border_radius=5,background_color=QColor(255,255,255))
        c.resize(150, 30)
        c.move(40+130, 190+100)
        c.setFont(font)
        c.setText("篮球🏀")

        c1 = CheckboxWidget(self)
        c1.resize(150, 30)
        c1.move(220+130, 190+100)
        c1.setFont(font)
        c1.setText("唱歌🎤")

        c2 = CheckboxWidget(self)
        c2.resize(150, 30)
        c2.move(220+130, 190+150)
        c2.setFont(font)
        c2.setText("跳舞💞")

        c3 = CheckboxWidget(self)
        c3.resize(150, 30)
        c3.move(40+130, 190+150)
        c3.setFont(font)
        c3.setText("Rap🎶")


    def onSucceed(self):
        tip = TipsWidget(self)
        tip.setText("Success|Description of the success")
        tip.status = TipsStatus.Succeed
        tip.move(120, 20)
        tip.resize(420,30)
        tip.show()

    def onWarning(self):
        tip = TipsWidget(self)
        tip.setText("Warning|Description of the action warning")
        tip.status = TipsStatus.Warning
        tip.move(120, 50)
        tip.resize(420,30)

        tip.show()

    def onDangerous(self):
        tip = TipsWidget(self)
        tip.setText("Danger|Information description of hazards")
        tip.status = TipsStatus.Dangerous
        tip.move(120, 80)
        tip.resize(420,30)

        tip.show()



if __name__ == '__main__':
    app = QApplication([])

    widget = Window()

    widget.show()
    app.exec()