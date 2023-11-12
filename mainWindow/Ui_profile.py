# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\CTU\DBMS\project\mainwindow\profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Profile(object):
    def setupUi(self, Profile):
        Profile.setObjectName("Profile")
        Profile.resize(1039, 790)
        Profile.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Profile)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_email = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_5.addWidget(self.lineEdit_email, 1, 1, 1, 1)
        self.label_email = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.gridLayout_5.addWidget(self.label_email, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Profile)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/icon/message-outline-48.ico"))
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 15, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_birth = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_birth.setFont(font)
        self.label_birth.setObjectName("label_birth")
        self.gridLayout_3.addWidget(self.label_birth, 1, 1, 1, 3)
        self.lineEdit_birthDay = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_birthDay.setFont(font)
        self.lineEdit_birthDay.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_birthDay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_birthDay.setObjectName("lineEdit_birthDay")
        self.gridLayout_3.addWidget(self.lineEdit_birthDay, 2, 1, 1, 1)
        self.lineEdit_birthYear = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_birthYear.setFont(font)
        self.lineEdit_birthYear.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_birthYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_birthYear.setObjectName("lineEdit_birthYear")
        self.gridLayout_3.addWidget(self.lineEdit_birthYear, 2, 3, 1, 1)
        self.lineEdit_birthMonth = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_birthMonth.setFont(font)
        self.lineEdit_birthMonth.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_birthMonth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_birthMonth.setObjectName("lineEdit_birthMonth")
        self.gridLayout_3.addWidget(self.lineEdit_birthMonth, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Profile)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/icon/birthday-cake-48.ico"))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 13, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Profile)
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/images/male.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(30, 65, 254);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 28, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 27, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_phone = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout_6.addWidget(self.label_phone, 0, 1, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout_6.addWidget(self.lineEdit_phone, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Profile)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icon/icon/phone-68-48.ico"))
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 17, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 29, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 4, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_lastname = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_lastname.setFont(font)
        self.lineEdit_lastname.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.gridLayout_2.addWidget(self.lineEdit_lastname, 1, 0, 1, 1)
        self.label_lastname = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lastname.setFont(font)
        self.label_lastname.setObjectName("label_lastname")
        self.gridLayout_2.addWidget(self.label_lastname, 0, 0, 1, 1)
        self.label_firstname = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_firstname.setFont(font)
        self.label_firstname.setObjectName("label_firstname")
        self.gridLayout_2.addWidget(self.label_firstname, 0, 1, 1, 1)
        self.lineEdit_firstname = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_firstname.setFont(font)
        self.lineEdit_firstname.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.gridLayout_2.addWidget(self.lineEdit_firstname, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_ward = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ward.setFont(font)
        self.label_ward.setObjectName("label_ward")
        self.gridLayout_8.addWidget(self.label_ward, 2, 1, 1, 1)
        self.comboBox_district = QtWidgets.QComboBox(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_district.setFont(font)
        self.comboBox_district.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.comboBox_district.setObjectName("comboBox_district")
        self.gridLayout_8.addWidget(self.comboBox_district, 1, 1, 1, 1)
        self.comboBox_ward = QtWidgets.QComboBox(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ward.setFont(font)
        self.comboBox_ward.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.comboBox_ward.setObjectName("comboBox_ward")
        self.gridLayout_8.addWidget(self.comboBox_ward, 3, 1, 1, 1)
        self.lineEdit_street = QtWidgets.QLineEdit(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_street.setFont(font)
        self.lineEdit_street.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.gridLayout_8.addWidget(self.lineEdit_street, 5, 1, 1, 1)
        self.label_district = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_district.setFont(font)
        self.label_district.setObjectName("label_district")
        self.gridLayout_8.addWidget(self.label_district, 0, 1, 1, 1)
        self.label_street = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_street.setFont(font)
        self.label_street.setObjectName("label_street")
        self.gridLayout_8.addWidget(self.label_street, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Profile)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icon/icon/apartment-48.ico"))
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 2, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 26, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(Profile)
        self.label.setMinimumSize(QtCore.QSize(48, 48))
        self.label.setMaximumSize(QtCore.QSize(48, 48))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/icon/gender-48.ico"))
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 2, 1)
        self.label_gender = QtWidgets.QLabel(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.gridLayout_4.addWidget(self.label_gender, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Profile)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 246, 247);\n"
"border: 1px solid rgb(116, 30, 240);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 7, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 18, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 16, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 14, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 8, 1, 1, 1)

        self.retranslateUi(Profile)
        QtCore.QMetaObject.connectSlotsByName(Profile)

    def retranslateUi(self, Profile):
        _translate = QtCore.QCoreApplication.translate
        Profile.setWindowTitle(_translate("Profile", "Form"))
        self.label_email.setText(_translate("Profile", "Email"))
        self.label_birth.setText(_translate("Profile", "Ngày sinh"))
        self.pushButton.setText(_translate("Profile", "Save changes"))
        self.label_phone.setText(_translate("Profile", "Số điện thoại"))
        self.label_lastname.setText(_translate("Profile", "Họ"))
        self.label_firstname.setText(_translate("Profile", "Tên"))
        self.label_ward.setText(_translate("Profile", "Phường/Xã"))
        self.label_district.setText(_translate("Profile", "Quận/Huyện"))
        self.label_street.setText(_translate("Profile", "Đường"))
        self.label_gender.setText(_translate("Profile", "Giới tính"))
        self.comboBox.setItemText(0, _translate("Profile", "Nam"))
        self.comboBox.setItemText(1, _translate("Profile", "Nữ"))
        self.comboBox.setItemText(2, _translate("Profile", "Khác"))
from mainwindow import profile_rsc_rc