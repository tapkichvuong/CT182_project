from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from muontra.Ui_ql_muontra import Ui_Muontra
from connector.mySql import mydb

class ql_muontra(QWidget):
    def __init__ (self):
        super(ql_muontra,self). __init__()
        self.ui = Ui_Muontra()
        self.ui.setupUi(self)
        self.handleLoadTinhTrang_CBB()
        self.ui.btn_timdg.clicked.connect(self.handleSearchDocGiaNhanh)
        self.ui.btn_timsach.clicked.connect(self.handleSearchSachNhanh)
        self.ui.btn_them.clicked.connect(self.addnewMuonSach)
        self.ui.btn_them.clicked.connect(self.handleSearchSachNhanh)
        self.ui.btn_tim_muon_tra.clicked.connect(self.handleSearchingLsMuon)
        self.ui.btn_update.clicked.connect(self.UpdateMT)
        self.ui.btn_update.clicked.connect(self.handleSearchingLsMuon)
        self.ui.btn_update.clicked.connect(self.handleSearchSachNhanh)
        self.ui.btn_them.clicked.connect(self.handleSearchingLsMuon)
        

#EDIT MUONTRA
    def UpdateMT(self):
        masach = self.ui.lineEdit_masach.text().strip()
        madocgia = self.ui.lineEdit_madocgia.text().strip()
        matt = self.ui.comboBox_tinhtrang.currentIndex()
        muon = {}
        muon['madocgia'] = madocgia
        muon['masach'] = masach
        muon['matt'] = matt
        if matt==1:
            db=mydb()
            msg = QMessageBox()
            checked = db.handleUpdateSachMuon(muon)
            if checked:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Success', 'trả sách thành công')
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.information(self,'Failed', 'trả sách thất bại,sách đã được trả hoặc không tồn tại') 
        elif matt==0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success','sách đang được mượn')
        elif matt==3:
            db=mydb()
            msg = QMessageBox()
            checked = db.handleUpdateMatHongSach(muon)
            if checked:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Success','Đã cập nhật tình trạng mất sách')
            else:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Failed','Cập nhật tình trạng mất sách thất bại')
        elif matt==4:
            db=mydb()
            msg = QMessageBox()
            checked = db.handleUpdateMatHongSach(muon)
            if checked:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Success','Đã cập nhật tình trạng hỏng sách')
            else:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Failed','Cập nhật tình trạng mất hỏng thất bại')
        elif matt==5:
            db=mydb()
            checked = db.handleUpdateMatHongSach(muon)
            msg = QMessageBox()
            if checked:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Success','Đã cập nhật tình trạng đền sách do mất')
            else:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Failed','Cập nhật thất bại')
        elif matt==6:
            db=mydb()
            checked = db.handleUpdateMatHongSach(muon)
            msg = QMessageBox()
            if checked:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Success','Đã cập nhật tình trạng đền sách do hỏng')
            else:
                msg.setIcon(QMessageBox.Information)
                msg.information(self,'Failed','Cập nhật thất bại')

#DELETE MUONTRA          
    def DeleteMT(self):
        db=mydb()
        msg = QMessageBox()
        masach = self.ui.lineEdit_masach.text()
        madocgia = self.ui.lineEdit_madocgia.text()
        check = db.handleXoaMT(masach,madocgia)
        # self.handleLoadMT()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Xóa thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Xóa thất bại')
#ADD MUON
    def addnewMuonSach(self):
        masach = self.ui.lineEdit_masach.text().strip()
        matt = 0
        madocgia = self.ui.lineEdit_madocgia.text()
        #them muon
        muon = {}
        muon['madocgia'] = madocgia
        muon['matt'] = matt
        muon['masach'] = masach
        db=mydb()
        msg = QMessageBox()
        checked = db.handleThemSachMuon(muon)
        # self.Reload_Page()
        if checked:
            
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'thêm thành công')
            
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'thêm thất bại sách không đủ số lượng hoặc chưa được trả')  
#lOAD TINH TRANG CBB
    def handleLoadTinhTrang_CBB(self):
        db=mydb()
        tt=db.handleLoadTinhTrang_CBB()
        # self.ui.comboBox_tinhtrang.addItem('')
        for tt in tt:
            self.ui.comboBox_tinhtrang.addItem(str(tt[1]),tt[0])
#TIM KIEM LICH SU MUON CUA DOC GIA 
    def handleSearchingLsMuon(self):
        db=mydb()
        madocgia = self.ui.lineEdit_madocgia.text().strip()
        masach = self.ui.lineEdit_masach.text().strip()
        data = db.handleTimLsMuon(madocgia, masach)
        self.ui.tbl_muontra.setRowCount(len(data))
        tablerow=0
        for row in data:
                self.ui.tbl_muontra.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.ui.tbl_muontra.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.ui.tbl_muontra.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
                self.ui.tbl_muontra.setItem(tablerow, 3, QTableWidgetItem(row[3]))
                self.ui.tbl_muontra.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
                self.ui.tbl_muontra.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
                self.ui.tbl_muontra.setItem(tablerow, 6, QTableWidgetItem(row[6]))
                tablerow+=1  
#TIM KIEM SACH NHANH
    def handleSearchSachNhanh(self):
        db=mydb()
        masach = self.ui.lineEdit_masach.text().strip()
        data = db.handleSearchSachNhanh(masach)
        self.ui.table_sach.setRowCount(len(data))
        tablerow=0
        for row in data:
            self.ui.table_sach.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.table_sach.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.table_sach.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
#TIM KIEM DOC GIA NHANH
    def handleSearchDocGiaNhanh(self):
        db=mydb()
        madocgia = self.ui.lineEdit_madocgia.text().strip()
        data = db.handleSearchDocGiaNhanh(madocgia)
        self.ui.table_docgia.setRowCount(len(data))
        tablerow=0
        for row in data:
            self.ui.table_docgia.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.table_docgia.setItem(tablerow, 1, QTableWidgetItem(row[1]))
#RELOAD PAGE MUON TRA
    def Reload_Page(self):
        self.ui.comboBox_tinhtrang.setCurrentIndex(0)
        self.ui.lineEdit_masach.setText("")
        self.ui.lineEdit_madocgia.setText("")