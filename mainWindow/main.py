import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from hashlib import sha256

from mainwindow.Ui_sidebar import Ui_MainWindow
from mainwindow.Ui_qlsach import Ui_Form
from mainwindow.Ui_ql_tp_sach import Ui_ql_tp_sach
from mainwindow.Ui_change_password import Ui_change_pass_page
from connector.mySql import mydb

class change_password(QWidget):
    def __init__ (self, logged_in_user):
        super(change_password,self). __init__()
        self.ui = Ui_change_pass_page()
        self.ui.setupUi(self)
        self.madocgia = logged_in_user
        self.ui.changePass_Btn.clicked.connect(self.changePassword)
        
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

class ql_tp_sach(QWidget):
    def __init__ (self):
        super(ql_tp_sach,self). __init__()
        self.ui = Ui_ql_tp_sach()
        self.ui.setupUi(self)
        self.ui.tableWidget_nxb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_TacGia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_theLoai.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.handleLoadNXB_table()
        self.handleLoadTacGia_table()
        self.handleLoadTheLoai_table()
        self.ui.pushButton_addnxb.clicked.connect(self.handleAddNXB)
        self.ui.pushButton_addTacGia.clicked.connect(self.handleAddTacGia)
        self.ui.pushButton_addTheLoai.clicked.connect(self.handleAddTheLoai)
        
        self.ui.pushButton_editnxb.clicked.connect(self.handleEditNXB)
        self.ui.pushButton_editTacGia.clicked.connect(self.handleEditTacGia)
        self.ui.pushButton_editTheLoai.clicked.connect(self.handleEditTheLoai)
        
        self.ui.pushButton_deletenxb.clicked.connect(self.handleDeleteNXB)
        self.ui.pushButton_deleteTacGia.clicked.connect(self.handleDeleteTacGia)
        self.ui.pushButton_deleteTheLoai.clicked.connect(self.handleDeleteTheloai)
        
        self.ui.pushButton_timnxb.clicked.connect(self.handleSearchingNXB)
        self.ui.pushButton_timTacGia.clicked.connect(self.handleSearchingTacGia)
        self.ui.pushButton_theLoai.clicked.connect(self.handleSearchingTheLoai)
       
    def handleLoadTacGia_table(self):
        db= mydb()
        tacgia=db.handleLoadTacGia()
        self.ui.tableWidget_TacGia.setRowCount(len(tacgia))
        tablerow=0
        for tacgia in tacgia:
            self.ui.tableWidget_TacGia.setItem(tablerow, 0, QTableWidgetItem(str(tacgia[0])))
            self.ui.tableWidget_TacGia.setItem(tablerow, 1, QTableWidgetItem(str(tacgia[1])))
            tablerow += 1

    def handleLoadNXB_table(self):
        db= mydb()
        nxb=db.handleLoadNXB()
        self.ui.tableWidget_nxb.setRowCount(len(nxb))
        tablerow=0
        for nxb in nxb:
            self.ui.tableWidget_nxb.setItem(tablerow, 0, QTableWidgetItem(str(nxb[0])))
            self.ui.tableWidget_nxb.setItem(tablerow, 1, QTableWidgetItem(str(nxb[1])))
            tablerow += 1
            
    def handleLoadTheLoai_table(self):
        db= mydb()
        tl=db.handleLoadTheLoai()
        self.ui.tableWidget_theLoai.setRowCount(len(tl))
        tablerow=0
        for tl in tl:
            self.ui.tableWidget_theLoai.setItem(tablerow, 0, QTableWidgetItem(str(tl[0])))
            self.ui.tableWidget_theLoai.setItem(tablerow, 1, QTableWidgetItem(str(tl[1])))
            tablerow += 1
    
    def handleAddNXB(self):
        db=mydb()
        msg = QMessageBox()
        tennxb = self.ui.lineEdit_tennxb.text().strip()
        check = db.handleThemNXB(tennxb)
        self.handleLoadNXB_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Thêm nhà xuất bản thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Thêm nhà xuất bản thất bại')
        
    def handleAddTacGia(self):
        db=mydb()
        msg = QMessageBox()
        tenTacGia = self.ui.lineEdit_tenTacGia.text().strip()
        check = db.handleThemTacGia(tenTacGia)
        self.handleLoadTacGia_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Thêm tác giả thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Thêm tác giả thất bại')
        
    def handleAddTheLoai(self):
        db=mydb()
        msg = QMessageBox()
        tenTheLoai = self.ui.lineEdit_tenTheLoai.text().strip()
        check = db.handleThemTheLoai(tenTheLoai)
        self.handleLoadTheLoai_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Thêm thể loại thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Thêm thể loại thất bại')
        
    def handleEditNXB(self):
        db=mydb()
        msg = QMessageBox()
        manxb = self.ui.lineEdit_manxb.text().strip()
        tennxb = self.ui.lineEdit_tennxb.text().strip()
        check = db.handleSuaNXB(manxb, tennxb)
        self.handleLoadNXB_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa nhà xuất bản thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa nhà xuất bản thất bại')
        
    def handleEditTacGia(self):
        db=mydb()
        msg = QMessageBox()
        maTacGia = self.ui.lineEdit_maTacGia.text().strip()
        tenTacGia = self.ui.lineEdit_tenTacGia.text().strip()
        check = db.handleTimTacGia(maTacGia, tenTacGia)
        self.handleLoadTacGia_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa tác giả thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa tác giả thất bại')
        
    def handleEditTheLoai(self):
        db=mydb()
        msg = QMessageBox()
        maTheLoai = self.ui.lineEdit_maTheLoai.text().strip()
        tenTheLoai = self.ui.lineEdit_tenTheLoai.text().strip()
        check = db.handleTimTheLoai(maTheLoai, tenTheLoai)
        self.handleLoadTheLoai_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa thể loại thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa thể loại thất bại')
        
    def handleDeleteNXB(self):
        db=mydb()
        msg = QMessageBox()
        manxb = self.ui.lineEdit_manxb.text().strip()
        tennxb = self.ui.lineEdit_tennxb.text().strip()
        check = db.handleXoaNXB(manxb, tennxb)
        self.handleLoadNXB_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Xóa nhà xuất bản thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Xóa nhà xuất bản thất bại')
            
    def handleDeleteTacGia(self):
        db=mydb()
        msg = QMessageBox()
        maTacGia = self.ui.lineEdit_maTacGia.text().strip()
        tenTacGia = self.ui.lineEdit_tenTacGia.text().strip()
        check = db.handleXoaTacGia(maTacGia, tenTacGia)
        self.handleLoadTacGia_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Xóa tác giả thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Xóa tác giả thất bại')
            
    def handleDeleteTheloai(self):
        db=mydb()
        msg = QMessageBox()
        maTheLoai = self.ui.lineEdit_maTheLoai.text().strip()
        tenTheLoai = self.ui.lineEdit_tenTheLoai.text().strip()
        check = db.handleXoaTheLoai(maTheLoai, tenTheLoai)
        self.handleLoadTheLoai_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Xóa thể loại thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Xóa thể loại thất bại')
            
    def handleSearchingNXB(self):
        db=mydb()
        manxb = self.ui.lineEdit_manxb.text().strip()
        tennxb = self.ui.lineEdit_tennxb.text().strip()
        data = db.handleTimNxb(manxb, tennxb)
        self.ui.tableWidget_nxb.setRowCount(len(data))
        tablerow=0
        for nxb in data:
            self.ui.tableWidget_nxb.setItem(tablerow, 0, QTableWidgetItem(str(nxb[0])))
            self.ui.tableWidget_nxb.setItem(tablerow, 1, QTableWidgetItem(str(nxb[1])))
            tablerow += 1
            
    def handleSearchingTacGia(self):
        db=mydb()
        maTacGia = self.ui.lineEdit_maTacGia.text().strip()
        tenTacGia = self.ui.lineEdit_tenTacGia.text().strip()
        data = db.handleTimTacGia(maTacGia, tenTacGia)
        self.ui.tableWidget_TacGia.setRowCount(len(data))
        tablerow=0
        for tacgia in data:
            self.ui.tableWidget_TacGia.setItem(tablerow, 0, QTableWidgetItem(str(tacgia[0])))
            self.ui.tableWidget_TacGia.setItem(tablerow, 1, QTableWidgetItem(str(tacgia[1])))
            tablerow += 1
            
    def handleSearchingTheLoai(self):
        db=mydb()
        maTheLoai = self.ui.lineEdit_maTheLoai.text().strip()
        tenTheLoai = self.ui.lineEdit_tenTheLoai.text().strip()
        data = db.handleTimTheLoai(maTheLoai, tenTheLoai)
        self.ui.tableWidget_theLoai.setRowCount(len(data))
        tablerow=0
        for loai in data:
            self.ui.tableWidget_theLoai.setItem(tablerow, 0, QTableWidgetItem(str(loai[0])))
            self.ui.tableWidget_theLoai.setItem(tablerow, 1, QTableWidgetItem(str(loai[1])))
            tablerow += 1

class qlsach(QWidget):
    def __init__ (self, main_window_instance):
        super(qlsach,self). __init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.ui.pushButton_them.clicked.connect(self.addnewbook)
        self.ui.pushButton_them.clicked.connect(self.handleLoadSach)
        self.handleLoadSach()
        self.handleLoadTacGia_CBB()
        self.handleLoadNXB_CBB()
        self.handleLoadTheLoai_CBB()
        self.main_window_instance = main_window_instance
        self.ui.pushButton_5.clicked.connect(self.redirect_to_ql_tp)
        self.ui.pushButton.clicked.connect(self.handleSearching)
    def addnewbook(self):
        tensach = self.ui.lineEdit_tensach.text()
        matacgia = self.ui.comboBox_1.currentIndex()
        manxb = self.ui.comboBox_2.currentIndex()
        matheloai = self.ui.comboBox_3.currentIndex()
        mota = self.ui.lineEdit_10.text()
        
        #them sach
        sach = {}
        sach['tensach'] = tensach
        sach['matacgia'] = matacgia
        sach['manxb'] = manxb
        sach['maloai'] = matheloai
        sach['mota'] = mota
        db = mydb()
        checked = db.handleThemSach(sach)
        
        
        
        

    def handleLoadTacGia_CBB(self):
        db= mydb()
        tacgia=db.handleLoadTacGia()
        self.ui.comboBox_1.addItem('')
        for tacgia in tacgia:
            self.ui.comboBox_1.addItem(str(tacgia[1]),str(tacgia[0]))
    def handleLoadNXB_CBB(self):
        db= mydb()
        nxb=db.handleLoadNXB()
        self.ui.comboBox_2.addItem('')
        for nxb in nxb:
            self.ui.comboBox_2.addItem(str(nxb[1]),str(nxb[0]))
    def handleLoadTheLoai_CBB(self):
        db= mydb()
        tl=db.handleLoadTheLoai()
        self.ui.comboBox_3.addItem('')
        for tl in tl:
            self.ui.comboBox_3.addItem(str(tl[1]),int(str(tl[0])))
    def handleLoadSach(self):
        db=mydb()
        data = db.handleLoadSach()
        self.ui.tableWidget.setRowCount(len(data))
        tablerow=0
        for row in data:
            self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            tablerow+=1
    #ham tim kiem sach
    def handleSearching(self):
        db=mydb()
        masach = self.ui.lineEdit.text().strip()
        tensach = self.ui.lineEdit_tensach.text().strip()
        tacgia = self.ui.comboBox_1.currentText()
        nxb = self.ui.comboBox_2.currentText()
        theloai = self.ui.comboBox_3.currentText()
        data = db.handleTimSach(masach, tensach, tacgia, nxb, theloai)
        self.ui.tableWidget.setRowCount(len(data))
        tablerow=0
        for row in data:
            self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            tablerow+=1
        
    def redirect_to_ql_tp(self):
        # Change the stackedWidget index in MainWindow to 7
        self.main_window_instance.ui.orders_btn_1.setChecked(False)
        self.main_window_instance.ui.orders_btn_2.setChecked(False)
        self.main_window_instance.ui.pushButton.setChecked(True)
        self.main_window_instance.ui.pushButton_2.setChecked(True)
        self.main_window_instance.ui.stackedWidget.setCurrentIndex(7)         
    

class MainWindow(QMainWindow):
    def __init__(self, login_instance):
        super(MainWindow, self).__init__()
        #get login user
        self.logged_in_user = login_instance
        #create GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.qlsach =qlsach(self)
        self.ui.gridLayout_4.addWidget(self.qlsach,0,0,1,1)
        self.ql_tp = ql_tp_sach()
        self.ui.gridLayout_9.addWidget(self.ql_tp, 0,0,1,1)
        self.change_pass_page = change_password(self.logged_in_user)
        self.ui.gridLayout_8.addWidget(self.change_pass_page, 0,0,1,1)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.login()
        
    ## lay ma doc gia
    def login(self):
        if self.logged_in_user:
            print(f"Logged in as {self.logged_in_user}")
        else:
            print("Authentication failed.")
    
    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def on_pushButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_pushButton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



