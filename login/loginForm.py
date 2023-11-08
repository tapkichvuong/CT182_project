import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit, QWidget)
from PyQt5.QtCore import QFile, QTextStream
from login.Ui_LoginWindow import Ui_Form
from login.RegisterForm import RegisterForm
from connector.mySql import mydb
class LoginForm(QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.LoginBtn.clicked.connect(self.handleLogin)
        self.ui.showPass.clicked.connect(self.toggleVisibility)
        self.ui.CreateBtn.clicked.connect(self.redirect_to_register)
        
    def toggleVisibility(self):
        if self.ui.lineEdit_pass.echoMode()==QLineEdit.Normal:
            self.ui.lineEdit_pass.setEchoMode(QLineEdit.Password)
        else:
            self.ui.lineEdit_pass.setEchoMode(QLineEdit.Normal)
                
    def handleLogin(self):
        msg = QMessageBox()
        db = mydb()
        checkPass = db.handleLogin(self.ui.lineEdit_name.text(), self.ui.lineEdit_pass.text())
        if checkPass:
            self.accept()
        else:
            msg.warning(self, 'Error', 'username or password is not correct')
    
    def redirect_to_register(self):
        QWidget.setVisible(self, False)
        self.register = RegisterForm()
        self.register.exec_()
        self.show()        
    def closeEvent(self, event):
        sys.exit()       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    loginWindow = LoginForm()
    loginWindow.show()
    
    sys.exit(app.exec())