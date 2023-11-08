import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit)
from PyQt5.QtCore import QFile, QTextStream
from Ui_RegisterWindow import Ui_Form
from connector.mySql import mydb
class RegisterForm(QDialog):
    def __init__(self):
        super(RegisterForm, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.LoginBtn.clicked.connect(self.close_window)
        self.ui.RegisterBtn.clicked.connect(self.registerMember)
        self.ui.showPass.clicked.connect(self.toggleVisibility)

    def registerMember(self):
        firstName = self.ui.lineEdit_firstname.text()
        lastName = self.ui.lineEdit_lastname.text()
        phone = self.ui.lineEdit_phone.text()
        email = self.ui.lineEdit_email.text()
        username = self.ui.lineEdit_userName.text()
        password = self.ui.lineEdit_pass.text()
        confirmPass = self.ui.lineEdit_confirmPass.text()
        msg = QMessageBox()
        if not firstName:
            msg.setIcon(QMessageBox.Warning)
            
            msg.warning(self, 'Error', 'First Name is empty')
            return
        if not lastName:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Last Name is empty')
            return
        if not phone:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Phone is empty')
            return
        if not email:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Email is empty')
            return
        if not username:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'User Name is empty')
            return
        if not password:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Password is empty')
            return
        if not confirmPass:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Confirm Password is empty')
            return
        if password != confirmPass:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Password and confirm password are not the same')
            return
        account = {}
        account['firstName'] = firstName
        account['lastName'] = firstName
        account['phone'] = phone
        account['email'] = email
        account['username'] = username
        account['pass'] = password
        db = mydb()
        db.handleRegister(account)
        msg.setIcon(QMessageBox.Information)
        msg.information(self,'Success', 'Account have been created')
        self.close_window()
        
    def toggleVisibility(self):
        if self.ui.lineEdit_pass.echoMode()==QLineEdit.Normal:
            self.ui.lineEdit_pass.setEchoMode(QLineEdit.Password)
            self.ui.lineEdit_confirmPass.setEchoMode(QLineEdit.Password)
        else:
            self.ui.lineEdit_pass.setEchoMode(QLineEdit.Normal)
            self.ui.lineEdit_confirmPass.setEchoMode(QLineEdit.Normal)

    def close_window(self):
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    loginWindow = RegisterForm()
    loginWindow.show()
    
    sys.exit(app.exec()) 