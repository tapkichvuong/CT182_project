from PyQt5.QtWidgets import QWidget, QMessageBox
from changePassword.Ui_change_password import Ui_change_pass_page
from hashlib import sha256
from connector.mySql import mydb

class change_password(QWidget):
    def __init__ (self, logged_in_user):
        super(change_password,self). __init__()
        self.ui = Ui_change_pass_page()
        self.ui.setupUi(self)
        self.madocgia = logged_in_user
        self.ui.changePass_Btn.clicked.connect(self.changePassword)
#CHANGE PASSWORD        
    def changePassword(self):
        db = mydb()
        msg = QMessageBox()
        currentPass = db.getCurrentPassword(self.madocgia)
        oldPass = self.ui.lineEdit_oldPass.text().strip()
        newPass = self.ui.lineEdit_newPass.text().strip()
        confirmPass = self.ui.lineEdit_confirmPass.text().strip()
        oldPass = sha256(oldPass.encode('utf-8')).hexdigest()
        if oldPass != currentPass:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Wrong password')
            return
        if newPass != confirmPass:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Password and confirm password are not the same')
            return
        db.changePassword(self.madocgia, newPass)
        msg.setIcon(QMessageBox.Information)
        msg.information(self,'Success', 'Password have been changed')