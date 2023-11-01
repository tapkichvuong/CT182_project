import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import QFile, QTextStream
from main import MainWindow

class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Library')
        layout = QGridLayout()
        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
        
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)
        
        button_login = QPushButton('Login')
        button_login.clicked.connect(self.handleLogin)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        self.setLayout(layout)
        self.show()
        
    def handleLogin(self):
        msg = QMessageBox()
        if self.lineEdit_username.text() == '1' and self.lineEdit_password.text() == '1':
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
    