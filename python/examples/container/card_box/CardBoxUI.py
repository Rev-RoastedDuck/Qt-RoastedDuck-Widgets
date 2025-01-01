# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardBox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from rrd_widgets import ComboBoxWidget, SimpleLineEdit_1


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(229, 235)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_11 = QWidget(Form)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMinimumSize(QSize(0, 21))
        self.widget_11.setMaximumSize(QSize(16777215, 21))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_serier_port_2 = QLabel(self.widget_11)
        self.label_serier_port_2.setObjectName(u"label_serier_port_2")
        sizePolicy.setHeightForWidth(self.label_serier_port_2.sizePolicy().hasHeightForWidth())
        self.label_serier_port_2.setSizePolicy(sizePolicy)
        self.label_serier_port_2.setMinimumSize(QSize(50, 0))
        self.label_serier_port_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_serier_port_2)

        self.comboBox_data_pos = ComboBoxWidget(self.widget_11)
        self.comboBox_data_pos.setObjectName(u"comboBox_data_pos")
        sizePolicy.setHeightForWidth(self.comboBox_data_pos.sizePolicy().hasHeightForWidth())
        self.comboBox_data_pos.setSizePolicy(sizePolicy)
        self.comboBox_data_pos.setMinimumSize(QSize(90, 0))
        self.comboBox_data_pos.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox_data_pos)


        self.verticalLayout.addWidget(self.widget_11, 0, Qt.AlignHCenter)

        self.widget_12 = QWidget(Form)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setMinimumSize(QSize(0, 21))
        self.widget_12.setMaximumSize(QSize(16777215, 21))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_serier_baudrate_2 = QLabel(self.widget_12)
        self.label_serier_baudrate_2.setObjectName(u"label_serier_baudrate_2")
        sizePolicy.setHeightForWidth(self.label_serier_baudrate_2.sizePolicy().hasHeightForWidth())
        self.label_serier_baudrate_2.setSizePolicy(sizePolicy)
        self.label_serier_baudrate_2.setMinimumSize(QSize(50, 0))
        self.label_serier_baudrate_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.label_serier_baudrate_2)

        self.comboBox_data_type = ComboBoxWidget(self.widget_12)
        self.comboBox_data_type.setObjectName(u"comboBox_data_type")
        sizePolicy.setHeightForWidth(self.comboBox_data_type.sizePolicy().hasHeightForWidth())
        self.comboBox_data_type.setSizePolicy(sizePolicy)
        self.comboBox_data_type.setMinimumSize(QSize(90, 0))
        self.comboBox_data_type.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_18.addWidget(self.comboBox_data_type)


        self.verticalLayout.addWidget(self.widget_12, 0, Qt.AlignHCenter)

        self.widget_15 = QWidget(Form)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setMinimumSize(QSize(0, 21))
        self.widget_15.setMaximumSize(QSize(16777215, 21))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_serier_baudrate_4 = QLabel(self.widget_15)
        self.label_serier_baudrate_4.setObjectName(u"label_serier_baudrate_4")
        sizePolicy.setHeightForWidth(self.label_serier_baudrate_4.sizePolicy().hasHeightForWidth())
        self.label_serier_baudrate_4.setSizePolicy(sizePolicy)
        self.label_serier_baudrate_4.setMinimumSize(QSize(50, 0))
        self.label_serier_baudrate_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.label_serier_baudrate_4)

        self.lineEdit_data = SimpleLineEdit_1(self.widget_15)
        self.lineEdit_data.setObjectName(u"lineEdit_data")
        self.lineEdit_data.setMinimumSize(QSize(90, 0))
        self.lineEdit_data.setMaximumSize(QSize(90, 27))

        self.horizontalLayout_19.addWidget(self.lineEdit_data)


        self.verticalLayout.addWidget(self.widget_15, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_serier_port_2.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u4f4d\u7f6e", None))
        self.label_serier_baudrate_2.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u7c7b\u578b", None))
        self.label_serier_baudrate_4.setText(QCoreApplication.translate("Form", u"\u5185\u5bb9", None))
    # retranslateUi

