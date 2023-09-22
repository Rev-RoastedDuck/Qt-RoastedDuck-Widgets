# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1006, 552)
        Form.setStyleSheet(u"#frame{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"#label{\n"
"	border-radius:13px;\n"
"	background-color: rgb(255, 255, 0);\n"
"\n"
"}\n"
"#label_2,#label_3{\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	border-radius:18px;\n"
"	background-color: rgba(198, 198, 198, 150);\n"
"}\n"
"#frame_3,#frame_4,#frame_5{\n"
"	border-radius:5px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 80, 901, 230))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 0, 500, 200))
        self.label.setMinimumSize(QSize(500, 0))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 381, 150))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 20, 381, 150))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(82, 80, 36, 36))
        icon = QIcon()
        icon.addFile(u":/icon/icon_png/\u540e\u9000 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(18, 18))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(803, 80, 36, 36))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon_png/\u524d\u8fdb (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(18, 18))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(380, 200, 160, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(120, 10, 10, 10))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(75, 10, 10, 10))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 10, 10, 10))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

