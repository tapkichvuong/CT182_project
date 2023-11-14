import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from home.Ui_home import Ui_Home

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        