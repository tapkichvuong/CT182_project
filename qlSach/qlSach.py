from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from qlSach.Ui_qlsach import Ui_Form
from connector.mySql import mydb

class qlsach(QWidget):
    def __init__ (self, main_window_instance):
        super(qlsach,self). __init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.ui.pushButton_them.clicked.connect(self.addnewbook)
        self.ui.pushButton_2.clicked.connect(self.DeleteSach)
        self.ui.pushButton_3.clicked.connect(self.UpdateSach)
        self.handleLoadSach()
        self.handleLoadTacGia_CBB()
        self.handleLoadNXB_CBB()
        self.handleLoadTheLoai_CBB()
        self.main_window_instance = main_window_instance
        self.ui.pushButton_5.clicked.connect(self.redirect_to_ql_tp)
        self.ui.pushButton_6.clicked.connect(self.Reload_Page)
        self.ui.pushButton.clicked.connect(self.handleSearching)
#EDIT SACH
    def UpdateSach(self):
        masach = self.ui.lineEdit_masach.text().strip()
        tensach = self.ui.lineEdit_tensach.text().strip()
        matacgia = self.ui.comboBox_1.currentIndex()
        manxb = self.ui.comboBox_2.currentIndex()
        maloai = self.ui.comboBox_3.currentIndex()
        mota = self.ui.lineEdit_10.text().strip()
        sl = self.ui.lineEdit_11.text().strip()
        # sl = self
        db=mydb()
        msg = QMessageBox()
        checked = db.handleUpdateSach(masach,tensach,matacgia,manxb,maloai,mota,sl)
        self.Reload_Page()

        if checked:
            
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'sửa sách thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'sửa sách thất bại')  
#DELETE SACH          
    def DeleteSach(self):
        db=mydb()
        msg = QMessageBox()
        masach = self.ui.lineEdit_masach.text()
        check = db.handleXoaSach(masach)
        self.handleLoadSach()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Xóa sách thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Xóa sách thất bại')
#ADD SACH
    def addnewbook(self):
        tensach = self.ui.lineEdit_tensach.text()
        matacgia = self.ui.comboBox_1.currentIndex()
        manxb = self.ui.comboBox_2.currentIndex()
        matheloai = self.ui.comboBox_3.currentIndex()
        sl=self.ui.lineEdit_11.text()
        mota = self.ui.lineEdit_10.text()
        #them sach

        sach = {}
        sach['tensach'] = tensach
        sach['matacgia'] = matacgia
        sach['manxb'] = manxb
        sach['maloai'] = matheloai
        sach['sl'] = sl
        sach['mota'] = mota
       
        db=mydb()
        msg = QMessageBox()
        checked = db.handleThemSach(sach)
        self.Reload_Page()
        if checked:
            
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'thêm sách thành công')
            
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'thêm sách thất bại')  
#lOAD TACGIA CBB
    def handleLoadTacGia_CBB(self):
        
        db= mydb()
        tacgia=db.handleLoadTacGia()
        self.ui.comboBox_1.addItem('')
        
        for tacgia in tacgia:
            self.ui.comboBox_1.addItem(str(tacgia[1]),tacgia[0])
#LOAD NXB CBB
    def handleLoadNXB_CBB(self):
        db= mydb()
        nxb=db.handleLoadNXB()
        self.ui.comboBox_2.addItem('')
        for nxb in nxb:
            self.ui.comboBox_2.addItem(str(nxb[1]),nxb[0])
#LOAD THE LOAI CBB
    def handleLoadTheLoai_CBB(self):
        db= mydb()
        tl=db.handleLoadTheLoai()
        self.ui.comboBox_3.addItem('')
        for tl in tl:
            self.ui.comboBox_3.addItem(str(tl[1]),tl[0])

#LOAD LAI TABLE SACH
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
            self.ui.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget.setItem(tablerow, 6, QTableWidgetItem(row[6]))
            tablerow+=1
#TIM KIEM SACH
    def handleSearching(self):
        db=mydb()
        masach = self.ui.lineEdit_masach.text().strip()
        tensach = self.ui.lineEdit_tensach.text().strip()
        tacgia = self.ui.comboBox_1.currentText()
        nxb = self.ui.comboBox_2.currentText()
        theloai = self.ui.comboBox_3.currentText()
        
        data = db.handleTimSach(masach, tensach, tacgia, nxb, theloai)
        self.ui.tableWidget.setRowCount(len(data))
        tablerow=0
        for row in data:
            if len(data)==1:
                self.ui.lineEdit_masach.setText(str(row[0]))
                self.ui.lineEdit_tensach.setText(row[1])
                self.ui.comboBox_1.setCurrentText(str(row[3]))
                self.ui.comboBox_2.setCurrentText(str(row[2]))
                self.ui.comboBox_3.setCurrentText(str(row[4]))
                self.ui.lineEdit_11.setText(str(row[5]))
                self.ui.lineEdit_10.setText(row[6])

                self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                self.ui.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
                self.ui.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
                self.ui.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
                self.ui.tableWidget.setItem(tablerow, 6, QTableWidgetItem(row[6]))
            else:
                # self.ui.lineEdit_masach.setText('')
                # self.ui.lineEdit_tensach.setText('')
                # self.handleLoadTacGia_CBB()
                # self.handleLoadNXB_CBB()
                # self.handleLoadTheLoai_CBB()
                # self.ui.lineEdit_10.setText('')
                self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                self.ui.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
                self.ui.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
                self.ui.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
                self.ui.tableWidget.setItem(tablerow, 6, QTableWidgetItem(row[6]))
                tablerow+=1
#CHUYEN HUONG DEN QL_TP       
    def redirect_to_ql_tp(self):
        # Change the stackedWidget index in MainWindow to 7
        self.main_window_instance.ui.orders_btn_1.setChecked(False)
        self.main_window_instance.ui.orders_btn_2.setChecked(False)
        self.main_window_instance.ui.pushButton.setChecked(True)
        self.main_window_instance.ui.pushButton_2.setChecked(True)
        self.main_window_instance.ui.stackedWidget.setCurrentIndex(7)           
#RELOAD PAGE SACH

    def Reload_Page(self):
        self.handleLoadSach()
        self.ui.comboBox_1.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.comboBox_3.setCurrentIndex(0)
        self.ui.lineEdit_masach.setText("")
        self.ui.lineEdit_tensach.setText("")
        self.ui.lineEdit_10.setText("")
        self.ui.lineEdit_11.setText("")