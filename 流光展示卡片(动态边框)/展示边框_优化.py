import sys
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QLabel
from PySide6.QtCore import Qt, QTimer, QRegularExpression, QRect
from PySide6.QtGui import QPainter, QColor, QConicalGradient, QPainterPath,QFont


#配置参数的时候，只要配置样式表就可以了

class DynamicBorderFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animationConfig()

    def ui(self):
        self.top_frame = QFrame(self)
        self.top_frame.setStyleSheet(f"background-color:#151a1a;border-radius:{self.son_frame_border_radius}px;")
        self.top_frame.setGeometry(self.Rborder_width, self.Rborder_width, self.width() - self.Rborder_width * 2, self.height() - self.Rborder_width * 2)

    def animationConfig(self):
        self.angle = 0 # 旋转的角度
        self.timer = QTimer() # 定时
        self.timer.timeout.connect(self.update)
        self.timer.start(20)

    def setStyleSheetConfig(self):
        '''
        正则提取样式
        :return:
        '''
        radius_match = QRegularExpression(r"border-radius:(?P<border_radius>\d+)px;")
        radius_result = radius_match.match(self.styleSheet())
        if radius_result.hasMatch():
            self.bottom_border_radius = int(radius_result.captured("border_radius"))

        Rborder_width_match = QRegularExpression(r"Rborder-width:(?P<Rborder_width>\d+)px;")
        Rborder_width_result = Rborder_width_match.match(self.styleSheet())
        if Rborder_width_result.hasMatch():
            self.Rborder_width = int(Rborder_width_result.captured("Rborder_width"))

        self.son_frame_border_radius = self.bottom_border_radius - self.Rborder_width

        Rcolor_match = QRegularExpression(r"Rcolor:rgba\((?P<Rcolor_1>.*?)\),rgba\((?P<Rcolor_2>.*?)\);")
        Rcolor_result = Rcolor_match.match(self.styleSheet())
        if Rcolor_result.hasMatch():
            self.color_1 = QColor(*[int(v) for v in Rcolor_result.captured("Rcolor_1").split(",")])
            self.color_2 = QColor(*[int(v) for v in Rcolor_result.captured("Rcolor_2").split(",")])

        self.son_frame_border_radius = self.bottom_border_radius - self.Rborder_width

        self.ui()

    def paintEvent(self, event):
        super(DynamicBorderFrame, self).paintEvent(event)


        # 配置绘画路径 -> 在圆角矩形内绘画
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.bottom_border_radius, self.bottom_border_radius)

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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 500)
        self.setStyleSheet("background-color:rgba(0,0,0,0);")

        frame = DynamicBorderFrame(self)
        # Rborder-width:卡片的边框宽度
        # Rcolor:流光的颜色
        # 背景颜色/流光颜色
        frame.setStyleSheet("background-color:rgba(0,0,0,255);border-radius:15px;Rborder-width:4px;Rcolor:rgba(153,0,51,255),rgba(255,153,0,255);")
        frame.setGeometry(100, 100, 200, 300)
        frame.setStyleSheetConfig() # 配置好后，需要调用setStyleSheetConfig()

        # 添加label到frame.top_frame
        self.label = QLabel(frame.top_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, frame.top_frame.width(), frame.top_frame.height())) # 0,0 是相对于frame.top_frame的位置坐标
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(100)
        self.label.setFont(font)
        # 字体颜色
        # 卡片背景颜色
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                 "background-color: #006633;\n"
                                 "border-radius:10px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
