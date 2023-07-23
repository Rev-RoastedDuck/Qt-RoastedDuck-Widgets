# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_btn.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Property, QAbstractAnimation, QPropertyAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QPainterPath)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
                               QSizePolicy, QWidget, QLabel)
import icon

from custom_btn import MyFrame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")


        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(310, 150, 141, 271))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	border-radius: 15px;\n"
"	background-color: rgba(255, 116, 0,200);\n"
"}\n"
"\n"
"#pushButton_8,#pushButton_6,#pushButton_7,#pushButton_9,#pushButton_10,#pushButton_11{\n"
"		\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgba(255, 116, 0,255);\n"
"	    border-radius: 10px;\n"
"		border: aqua solid 1px;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)


        self.frame = MyFrame(self.frame_6,text="Close",icon=":/icon/\u56fe\u6807/\u5173\u95ed (1).png")

        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 110, 30))


        self.frame_2 = MyFrame(self.frame_6,text="Enter",icon=":/icon/\u56fe\u6807/\u767b\u5f55.png")
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 110, 30))


        self.frame_3 = MyFrame(self.frame_6,text="SetKey",icon=":/icon/\u56fe\u6807/\u786e\u8ba4\u5bc6\u7801.png")
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 100, 110, 30))

        self.frame_4 = MyFrame(self.frame_6,text="Resign",icon=":/icon/\u56fe\u6807/\u4f1a\u5458\u6ce8\u518c\u767b\u5f55\u7ba1\u7406.png")
        self.frame_4.setGeometry(QRect(10, 140, 110, 30))

        self.frame_5 = MyFrame(self.frame_6,text="Verify",icon=":/icon/\u56fe\u6807/\u9a8c\u8bc1 \u9a8c\u8bc1\u7801.png")
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 180, 110, 30))

        self.frame_7 = MyFrame(self.frame_6,text="Share",icon=":/icon/\u56fe\u6807/\u5206\u4eab.png")
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 220, 110, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))