# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\CTU\DBMS\project\mainwindow\statistic.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statistic(object):
    def setupUi(self, Statistic):
        Statistic.setObjectName("Statistic")
        Statistic.resize(710, 644)
        self.gridLayout_4 = QtWidgets.QGridLayout(Statistic)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_pie = QtWidgets.QGridLayout()
        self.gridLayout_pie.setObjectName("gridLayout_pie")
        self.pieChart_combo_box = QtWidgets.QComboBox(Statistic)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pieChart_combo_box.setFont(font)
        self.pieChart_combo_box.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;")
        self.pieChart_combo_box.setObjectName("pieChart_combo_box")
        self.gridLayout_pie.addWidget(self.pieChart_combo_box, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_pie, 1, 0, 1, 1)
        self.gridLayout_Line = QtWidgets.QGridLayout()
        self.gridLayout_Line.setObjectName("gridLayout_Line")
        self.year_combo_box = QtWidgets.QComboBox(Statistic)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.year_combo_box.setFont(font)
        self.year_combo_box.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;")
        self.year_combo_box.setObjectName("year_combo_box")
        self.gridLayout_Line.addWidget(self.year_combo_box, 0, 0, 1, 1)
        self.month_combo_box = QtWidgets.QComboBox(Statistic)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.month_combo_box.setFont(font)
        self.month_combo_box.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;")
        self.month_combo_box.setObjectName("month_combo_box")
        self.gridLayout_Line.addWidget(self.month_combo_box, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_Line, 2, 0, 1, 1)

        self.retranslateUi(Statistic)
        QtCore.QMetaObject.connectSlotsByName(Statistic)

    def retranslateUi(self, Statistic):
        _translate = QtCore.QCoreApplication.translate
        Statistic.setWindowTitle(_translate("Statistic", "Form"))
