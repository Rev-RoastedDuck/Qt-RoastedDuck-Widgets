from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QFontDatabase, QFont, QColor, Qt

from rrd_widgets import Speedometer1, Speedometer2, Speedometer3,Silder


class Window1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.uiInit()

    def uiInit(self):
        self.resize(550,340)
        self.setStyleSheet("background-color:rgb(255,255,255);")
        self.setWindowTitle("rrd-widgets")

        font_id = QFontDatabase.addApplicationFont("segoeuib.ttf")
        custom_font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
        custom_font.setPointSize(16)
        custom_font.setBold(True)

        """ 原点位置在组件(圆环)的中心 """

        self.speedometer_1 = Speedometer1(self)
        self.speedometer_1.setParams(color_arc_add=QColor(231, 227, 228), color_arc_sub=QColor(148, 59, 142),
                                     color_triangle=QColor(0, 0, 0), color_font=QColor(0, 0, 0), radius=60,
                                     text_height=30, text_y=5,text_unit="°")
        self.speedometer_1.move(20, 60)
        self.speedometer_1.setRange(0, 180)
        self.speedometer_1.updateValue(20)
        self.speedometer_1.setFont(custom_font)

        self.speedometer_2 = Speedometer2(self)
        self.speedometer_2.setParams(color_arc_add=QColor(231, 227, 228), color_arc_sub=QColor(148, 59, 142),
                                     color_triangle=QColor(0, 0, 0), color_font=QColor(0, 0, 0), radius=60,
                                     text_height=25, text_y=-22,text_unit="°")
        self.speedometer_2.move(190, 60)
        self.speedometer_2.setRange(0, 180)
        self.speedometer_2.updateValue(20)
        self.speedometer_2.setFont(custom_font)

        self.speedometer_3 = Speedometer3(self)
        self.speedometer_3.setParams(color_arc_add=QColor(231, 227, 228), color_arc_sub=QColor(148, 59, 142),
                                     color_triangle=QColor(0, 0, 0), color_font=QColor(0, 0, 0), radius=60,
                                     text_height=25, text_y=-22,text_unit="°")
        self.speedometer_3.move(360, 60)
        self.speedometer_3.setRange(0, 180)
        self.speedometer_3.updateValue(180)
        self.speedometer_3.setFont(custom_font)

        self.slider = Silder(Qt.Orientation.Horizontal,self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.resize(200, 30)
        self.slider.move(180, 260)

        self.slider.valueChanged.connect(self.updateValue)
    def updateValue(self,v):
        self.speedometer_1.updateValue(v)
        self.speedometer_2.updateValue(v)
        self.speedometer_3.updateValue(v)



if __name__ == '__main__':
    app = QApplication()
    s = Window1()
    s.show()
    app.exec()
