import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit)
from PyQt5.QtCore import QFile, QTextStream
from Ui_RegisterWindow import Ui_Form

class RegisterForm(QDialog):
    def __init__(self):
        super(RegisterForm, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.LoginBtn.clicked.connect(self.close_window)

    def close_window(self):
        self.close()