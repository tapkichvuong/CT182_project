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
        tacgia = self.ui.comboBox_1.currentText()
        nxb = self.ui.comboBox_2.currentText()
        theloai = self.ui.comboBox_3.currentText()
        data = db.handleTimSach(tacgia, nxb, theloai)
        print(data)
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



