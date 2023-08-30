import sys
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QLabel
from PySide6.QtCore import Qt, QTimer, QRegularExpression, QRect
from PySide6.QtGui import QPainter, QColor, QConicalGradient, QPainterPath, QFont, QPixmap

from GetStyleProperty import get_property,transfer_type

class DynamicBorderFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.componentInit()
        self.animationConfig()

    def componentInit(self):
        self.label = QLabel(self)

    def uiConfig(self):
        self.label.setGeometry(self.Rborder_width, self.Rborder_width, self.width() - self.Rborder_width * 2, self.height() - self.Rborder_width * 2)
        self.label.setStyleSheet(f"""
                                    color: {self.font_color};
                                    background-color: {self.inside_background_color};
                                    border-radius:{self.border_radius - 5}px;
                                  """
                                 )
        self.label.setAlignment(Qt.AlignCenter)

    def animationConfig(self):
        self.angle = 0
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update)

    def getStyleSheetConfig(self):
        '''
        提取样式
        :return:
        '''
        DynamicBorderFrame_property:dict = get_property(self)["DynamicBorderFrame"]

        self.font_color = DynamicBorderFrame_property["color"]
        self.color_1 = transfer_type(DynamicBorderFrame_property["Rcolor_1"],"color")
        self.color_2 = transfer_type(DynamicBorderFrame_property["Rcolor_2"],"color")
        self.inside_background_color = DynamicBorderFrame_property["inside-background-color"]
        self.border_radius = transfer_type(DynamicBorderFrame_property["border-radius"], "pixel")
        self.Rborder_width = transfer_type(DynamicBorderFrame_property["Rborder-width"],"pixel")

    def paintEvent(self, event):
        super(DynamicBorderFrame, self).paintEvent(event)

        # 配置绘画路径 -> 在圆角矩形内绘画
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.translate(self.width() / 2, self.height() / 2) # 把绘画原点移动到卡片中心
        painter.save()

        # 绘制第一条边框
        gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0) # 设置锥形渐变原点为卡片中心
        gradient.setColorAt(0, QColor(0,0,0,255))
        gradient.setColorAt(0.5, self.color_1)
        painter.setBrush(gradient)
        painter.rotate(self.angle) # 旋转画笔
        painter.drawRect(0, 0,self.width(),self.height())

        painter.restore()

        # 绘制第二条边框
        gradient.setColorAt(0, QColor(0,0,0,255))
        gradient.setColorAt(0.5, self.color_2)
        painter.setBrush(gradient)
        painter.rotate(self.angle+180)
        painter.drawRect(0, 0,self.width(),self.height())

        painter.restore()
        self.angle += 1

    def showEvent(self, event):
        super().showEvent(event)
        self.getStyleSheetConfig()
        self.uiConfig()
        self.timer.start()

    def setFont(self, font: QFont):
        self.label.setFont(font)

    def setText(self,text:str):
        self.label.setText(text)

    def setPixmap(self,pximap:QPixmap):
        self.label.setPixmap(pximap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    window.setGeometry(0, 0, 400, 500)
    window.setStyleSheet("background-color:rgba(0,0,0,0);")

    frame = DynamicBorderFrame(window)
    frame.setGeometry(100, 100, 200, 300)
    frame.setStyleSheet("DynamicBorderFrame{"
                        "   background-color:rgba(0,0,0,255);"
                        "   inside-background-color:#006633;"
                        "   border-radius:15px;"
                        "   Rborder-width:4px;"
                        "   Rcolor_1:rgba(153,0,51,255);"
                        "   Rcolor_2:rgba(255,153,0,255);"
                        "   color: rgb(255, 255, 255);}"
                        )
    font = QFont()
    font.setFamilies([u"Consolas"])
    font.setPointSize(100)
    frame.setFont(font)
    frame.setText("3")

    window.show()
    sys.exit(app.exec())
