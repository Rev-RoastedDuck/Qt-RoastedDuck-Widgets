from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
from rrd_widgets import AlertWidget,AlertWidgetStatus

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("window")
        self.setWindowTitle(" .")

        self.resize(650,400)
        self.setStyleSheet("QPushButton{"
                           "background-color:rgb(0, 129, 140);"
                           "color:#ffffff;"
                           "border-radius:5px;"
                           ""
                           "}"
                           "#window{"
                           "background-color:rgb(255,255,255);}"
                           ""
                           ""
                           "")

        font = QFont()
        font.setPointSize(10)

        s_btn = QPushButton(self)
        w_btn = QPushButton(self)
        d_btn = QPushButton(self)

        s_btn.clicked.connect(self.onSucceed)
        w_btn.clicked.connect(self.onWarning)
        d_btn.clicked.connect(self.onDangerous)

        s_btn.setGeometry(10+160,190+40,100,30)
        w_btn.setGeometry(120+160,190+40,100,30)
        d_btn.setGeometry(230+160,190+40,100,30)

        s_btn.setText("Succeed")
        d_btn.setText("Dangerous")
        w_btn.setText("Warning")

        s_btn.setFont(font)
        d_btn.setFont(font)
        w_btn.setFont(font)


    def onSucceed(self):
        tip = AlertWidget(self)
        tip.setText("Success|Description of the success")
        tip.status = AlertWidgetStatus.Succeed
        tip.move(120, 20)
        tip.show()

    def onWarning(self):
        tip = AlertWidget(self)
        tip.setText("Warning|Description of the action warning")
        tip.status = AlertWidgetStatus.Warning
        tip.move(120, 50)
        tip.show()

    def onDangerous(self):
        tip = AlertWidget(self)
        tip.setText("Danger|Information description of hazards")
        tip.status = AlertWidgetStatus.Dangerous
        tip.move(120, 80)
        tip.show()



if __name__ == '__main__':
    app = QApplication([])

    widget = Window()

    widget.show()
    app.exec()