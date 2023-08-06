"""
RButton.py
作者：Rev-RoastedDuck
csdnBlog: Rev_RoastDuck
WeChat:Roast_71
Email:2731491939@qq.com
"""
from PySide6.QtCore import  QPoint
from PySide6.QtCore import (QRect)
from PySide6.QtWidgets import (QFrame, QPushButton)

class RButton(QFrame):
    def __init__(self, size,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fixSize = size
        self.ui()

    def ui(self):
        self.setMaximumSize(self.fixSize)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(QPoint(0,0),self.fixSize))
        self.pushButton.setMaximumSize(self.fixSize)
        self.setStyleSheet("QPushButton{background-color:rgba(255,255,255,0)}")