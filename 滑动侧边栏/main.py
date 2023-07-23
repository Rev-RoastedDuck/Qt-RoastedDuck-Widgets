from PySide6.QtCore import QRect, QSize,  QPropertyAnimation, QAbstractAnimation, \
    QParallelAnimationGroup
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from ui import Ui_MainWindow
from custom_btn import MyFrame

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setStyleSheet(	"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,stop:0  #e60042,stop:0.05 #d40f52, stop:0.20 #c21d62, stop:0.31 #af2c72, stop:0.45   #7958a3, stop:0.79  #8b4993, stop:0.86  #6667b3, stop:0.935  #5475c3)};QPushButton{border-radius: 10px;background-color: rgba(255, 116, 0,0);color: rgb(255, 255, 255);")
        self.ui.setupUi(self)
        self.config_init()
        self.show()


    def enterEvent_frame(self, event):
        # 跳过第一次
        if not self.enterFlag:
            self.enterFlag = 1
            return
        super().enterEvent(event)
        # 显示包含文字的按钮
        for item in self.ui.frame_6.findChildren(MyFrame):
            item.pushButton_btn.show()

        self.animationGroup.setDirection(QAbstractAnimation.Backward)
        self.animationGroup.start()


    def leaveEvent_frame(self, event):
        super().leaveEvent(event)
        for item in self.ui.frame_6.findChildren(MyFrame):
            item.pushButton_btn.hide()

        self.animationGroup.setDirection(QAbstractAnimation.Forward)
        self.animationGroup.start()


    def config_init(self):
        # 设置变形部件尺寸
        self.mainFrame_height = self.ui.frame_6.height()
        self.mainFrame_widthHide = 61
        self.mainFrame_widthShow = self.ui.frame_6.width()
        self.mainFrame_widthChange = self.mainFrame_widthShow - self.mainFrame_widthHide
        self.mainFrame_xShow = self.ui.frame_6.geometry().x()
        self.mainFrame_xHide = self.ui.frame_6.geometry().x() + self.mainFrame_widthChange/2
        self.mainFrame_y = self.ui.frame_6.y()

        self.btnFrame_widthShow = self.ui.frame.width()
        self.btnFrame_widthHide = 40
        self.btnFrame_height = self.ui.frame.height()

        # 绑定鼠标进出侧边栏事件
        self.ui.frame_6.leaveEvent = self.leaveEvent_frame
        self.ui.frame_6.enterEvent = self.enterEvent_frame

        # 判断是否第一次进入
        self.enterFlag = 0

        # 动画
        self.animationGroup = QParallelAnimationGroup()
        self.animationGroup_function()


    def animationGroup_function(self):
        # 按钮动画
        for frame in self.ui.frame_6.children():
            if isinstance(frame,MyFrame):
                frame.btnAnimation = QPropertyAnimation(frame,b"size")
                frame.btnAnimation.setDuration(150)
                frame.btnAnimation.setStartValue(QSize(self.btnFrame_widthShow, self.btnFrame_height))
                frame.btnAnimation.setEndValue(QSize(self.btnFrame_widthHide, self.btnFrame_height))
                self.animationGroup.addAnimation(frame.btnAnimation)

        # 侧边栏动画
        self.frameAnimation = QPropertyAnimation()
        self.frameAnimation.setTargetObject(self.ui.frame_6)
        self.frameAnimation.setPropertyName(b"geometry")
        self.frameAnimation.setDuration(150)
        self.frameAnimation.setStartValue(
            QRect(self.mainFrame_xShow, self.mainFrame_y, self.mainFrame_widthShow, self.mainFrame_height))
        self.frameAnimation.setEndValue(
            QRect(self.mainFrame_xHide, self.mainFrame_y, self.mainFrame_widthHide, self.mainFrame_height))
        self.animationGroup.addAnimation(self.frameAnimation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    app.exec()