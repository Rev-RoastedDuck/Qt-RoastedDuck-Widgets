from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QApplication

from rrd_widgets import SwitchButton_1,SwitchButton_2,SwitchButton_3,SwitchButton_4,SwitchButton_5


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(300, 400)

        self.switchButton_1 = SwitchButton_1(parent=self)
        self.switchButton_1.setGeometry(80, 100, 60, 30)
        self.switchButton_1.setParams(checked_background_color=QColor(0, 89, 89),
                                      indicator_color=QColor(255, 255, 255),
                                      background_color=QColor(204, 204, 204),
                                      )

        self.switchButton_2 = SwitchButton_2(parent=self)
        self.switchButton_2.setGeometry(180, 100, 60, 30)
        self.switchButton_2.setParams(checked_background_color=QColor(0, 89, 89),
                                      checked_indicator_color=QColor(0, 89, 89),
                                      )

        self.switchButton_3 = SwitchButton_3(parent=self)
        self.switchButton_3.setGeometry(80, 150, 60, 30)
        self.switchButton_3.setParams(indicator_color=QColor(255, 255, 255),
                                      background_color=QColor(204,204,204),
                                      checked_background_color=QColor(0, 89, 89),
                                      checked_indicator_color=QColor(255, 255, 255))

        self.switchButton_4 = SwitchButton_4(parent=self)
        self.switchButton_4.setGeometry(180, 150, 60, 30)
        self.switchButton_4.setParams(checked_background_color=QColor(0, 89, 89),
                                      indicator_color=QColor(255, 255, 255),
                                      background_color=QColor(204,204,204),
                                      checked_indicator_color=QColor(255, 255, 255))

        self.switchButton_5 = SwitchButton_5(parent=self)
        self.switchButton_5.setGeometry(80, 200, 60, 30)
        self.switchButton_5.setParams(background_color=QColor(188, 188, 188),
                                      checked_background_color=QColor(0, 89, 89),
                                      indicator_color=QColor(255, 255, 255))


if __name__ == '__main__':
    app = QApplication()
    w = Window()
    w.show()
    app.exec()