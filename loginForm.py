import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox)
from PyQt5.QtCore import QFile, QTextStream
from main import MainWindow
from Ui_LoginWindow import Ui_Form
class LoginForm(QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.LoginBtn.clicked.connect(self.handleLogin)
        
    def handleLogin(self):
        msg = QMessageBox()
        if self.ui.lineEdit_name.text() == '1' and self.ui.lineEdit_pass.text() == '1':
            self.accept()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()
            
    def closeEvent(self, event):
        sys.exit()       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    while True:
        loginWindow = LoginForm()
        if loginWindow.exec_() == QDialog.Accepted:
            win = MainWindow()
            win.show()
            app.exec_()
    