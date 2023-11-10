import sys
from PyQt5.QtWidgets import (QApplication, QDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QTextStream
from mainwindow.main import MainWindow
from login.loginForm import LoginForm
import ctypes

#set taskbar icon
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)
#set app icon
app.setWindowIcon(QIcon('icon\Logo.ico'))
style_file = QFile("style.qss")
style_file.open(QFile.ReadOnly | QFile.Text)
style_stream = QTextStream(style_file)
app.setStyleSheet(style_stream.readAll())

while True:
    loginWindow = LoginForm()
    if loginWindow.exec_() == QDialog.Accepted:
        # truyen ma doc gia vao main
        win = MainWindow(loginWindow.madocgia)
        win.show()
        app.exec_()
    