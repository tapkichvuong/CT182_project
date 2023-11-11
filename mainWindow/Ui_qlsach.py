# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow\qlsach.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit, QWidget)
from connector.mySql import mydb

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


    
class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_10 = QtWidgets.QGridLayout(Form)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_masach = QtWidgets.QLineEdit(Form)
        self.lineEdit_masach.setObjectName("lineEdit_masach")
        self.gridLayout.addWidget(self.lineEdit_masach, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_tensach = QtWidgets.QLineEdit(Form)
        self.lineEdit_tensach.setObjectName("lineEdit_tensach")
        self.gridLayout_2.addWidget(self.lineEdit_tensach, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_1 = QtWidgets.QComboBox(Form)
        self.comboBox_1.setObjectName("comboBox_1")
        self.gridLayout_3.addWidget(self.comboBox_1, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_6.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 3, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 4, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_them = QtWidgets.QPushButton(Form)
        self.pushButton_them.setObjectName("pushButton_them")
        self.horizontalLayout.addWidget(self.pushButton_them)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_10.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout_10.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_9.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 3, 0, 1, 1)
        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Mã Sách"))
        self.label_2.setText(_translate("Form", "Tên Sách"))
        self.label_3.setText(_translate("Form", "Tác Giả"))
        self.label_6.setText(_translate("Form", "NXB"))
        self.label_7.setText(_translate("Form", "Thể Loại"))
        self.label_4.setText(_translate("Form", "Mô Tả"))
        self.pushButton_them.setText(_translate("Form", "Thêm"))
        self.pushButton_3.setText(_translate("Form", "Cập Nhật"))
        self.pushButton_2.setText(_translate("Form", "Xoá"))
        self.pushButton.setText(_translate("Form", "Tìm Kiếm"))
        self.pushButton_5.setText(_translate("Form", "QL Tác Giả,NXB,Thể Loại"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã Sách"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tên Sách"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "NXB"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tác Giả"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thể Loại"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Mô Tả"))
