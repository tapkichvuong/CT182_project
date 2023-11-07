import sys
from PyQt5.QtWidgets import (QApplication, QDialog)
from PyQt5.QtCore import QFile, QTextStream
from mainWindow.main import MainWindow
from login.loginForm import LoginForm

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
    