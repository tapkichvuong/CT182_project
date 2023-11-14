from PyQt5.QtWidgets import QWidget, QMessageBox
from myProfile.Ui_profile import Ui_Profile
from connector.mySql import mydb
from datetime import datetime

class profile(QWidget):
    def __init__ (self, logged_in_user):
        super(profile,self). __init__()
        self.ui = Ui_Profile()
        self.ui.setupUi(self)
        self.madocgia = logged_in_user
        self.handleLoadHuyen()
        self.ui.comboBox_district.currentIndexChanged.connect(self.updateComboPhuong)
        self.handleLoadProfile()
        self.ui.pushButton.clicked.connect(self.handleEditProfile)
#LOAD HUYEN    
    def handleLoadHuyen(self):
        db= mydb()
        districts = db.handleLoadHuyen()
        self.ui.comboBox_district.addItem('')
        for district in districts:
            self.ui.comboBox_district.addItem(str(district[1]),str(district[0]))
#UPDATE COMBO PHUONG              
    def updateComboPhuong(self, index):
        self.ui.comboBox_ward.clear()
        db= mydb()
        wards = db.handleLoadPhuong(index)
        self.ui.comboBox_ward.addItem('')
        for ward in wards:
            self.ui.comboBox_ward.addItem(str(ward[1]),str(ward[0]))
#LOAD PROFILE                 
    def handleLoadProfile(self):
        db = mydb()
        data = db.handleLoadProfile(self.madocgia)
        firstname = data[0]
        lastname = data[1]
        if(data[2] == 0):   gender = 'Nam'
        elif(data[2] == 1): gender ='Nữ'
        else: gender = 'Khác'
        birth_day = data[3]
        birth_month = data[4]
        birth_year = data[5]
        phone = data[6]
        email = data[7]
        huyen = data[8]
        phuong = data[9]
        diachi = data[10]
        self.ui.lineEdit_firstname.setText(firstname)
        self.ui.lineEdit_lastname.setText(lastname)
        self.ui.comboBox.setCurrentText(gender)
        self.ui.lineEdit_birthDay.setText(str(birth_day))
        self.ui.lineEdit_birthMonth.setText(str(birth_month))
        self.ui.lineEdit_birthYear.setText(str(birth_year))
        self.ui.lineEdit_phone.setText(phone)
        self.ui.lineEdit_email.setText(email)
        self.ui.lineEdit_street.setText(diachi)
        self.ui.comboBox_district.setCurrentText(huyen)
        self.ui.comboBox_ward.setCurrentText(phuong)
#EDIT PROFILE   
    def handleEditProfile(self):
        db= mydb()
        msg = QMessageBox()
        firstname = self.ui.lineEdit_firstname.text().strip()
        lastname =  self.ui.lineEdit_lastname.text().strip()
        gender = self.ui.comboBox.currentIndex()
        birthday = self.ui.lineEdit_birthYear.text().strip() + '-' + self.ui.lineEdit_birthMonth.text().strip() + '-' + self.ui.lineEdit_birthDay.text().strip()
        phone = self.ui.lineEdit_phone.text().strip()
        email = self.ui.lineEdit_email.text().strip()
        phuong = self.ui.comboBox_ward.currentText()
        diachi = self.ui.lineEdit_street.text().strip()
        print(firstname, lastname, gender, birthday, phone, email, phuong, diachi)
        if not firstname:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Họ không được trống')
            return
        if not lastname:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Tên không được trống')
            return
        if self.is_valid_date(birthday):
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Ngày sinh không hợp lệ')
            return
        if not phone:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Số điện thoại không được trống')
            return
        if not email:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Email không được trống')
            return
        if not phuong:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Phường không được trống')
            return
        if not diachi:
            msg.setIcon(QMessageBox.Warning)
            msg.warning(self, 'Error', 'Địa chỉ không được trống')
            return
        profile = {}
        profile['firstname'] = firstname
        profile['lastname'] = lastname
        profile['gender'] = gender
        profile['birthday'] = birthday
        profile['phone'] = phone
        profile['email'] = email
        profile['tenphuong'] = phuong
        profile['diachi'] = diachi
        check = db.handleEditProfile(self.madocgia, profile)
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa profile thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa profile thất bại')
#VALID DATE
    def is_valid_date(self, date_string):
        try:
            # Attempt to parse the date string
            datetime.strptime(date_string, '%y-%m-%d')
            return True
        except ValueError:
            # If parsing fails, it's an invalid date
            return False