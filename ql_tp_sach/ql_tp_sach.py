from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from ql_tp_sach.Ui_ql_tp_sach import Ui_ql_tp_sach
from connector.mySql import mydb

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
#LOAD TABLE TAC GIA      
    def handleLoadTacGia_table(self):
        db= mydb()
        tacgia=db.handleLoadTacGia()
        self.ui.tableWidget_TacGia.setRowCount(len(tacgia))
        tablerow=0
        for tacgia in tacgia:
            self.ui.tableWidget_TacGia.setItem(tablerow, 0, QTableWidgetItem(str(tacgia[0])))
            self.ui.tableWidget_TacGia.setItem(tablerow, 1, QTableWidgetItem(str(tacgia[1])))
            tablerow += 1
#LOAD TABLE NXB
    def handleLoadNXB_table(self):
        db= mydb()
        nxb=db.handleLoadNXB()
        self.ui.tableWidget_nxb.setRowCount(len(nxb))
        tablerow=0
        for nxb in nxb:
            self.ui.tableWidget_nxb.setItem(tablerow, 0, QTableWidgetItem(str(nxb[0])))
            self.ui.tableWidget_nxb.setItem(tablerow, 1, QTableWidgetItem(str(nxb[1])))
            tablerow += 1
#LOAD TABLE THE LOAI           
    def handleLoadTheLoai_table(self):
        db= mydb()
        tl=db.handleLoadTheLoai()
        self.ui.tableWidget_theLoai.setRowCount(len(tl))
        tablerow=0
        for tl in tl:
            self.ui.tableWidget_theLoai.setItem(tablerow, 0, QTableWidgetItem(str(tl[0])))
            self.ui.tableWidget_theLoai.setItem(tablerow, 1, QTableWidgetItem(str(tl[1])))
            tablerow += 1
#ADD NXB    
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
#ADD TACGIA        
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
#ADD THE LOAI       
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
#EDIT NXB       
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
#EDIT TAC GIA       
    def handleEditTacGia(self):
        db=mydb()
        msg = QMessageBox()
        maTacGia = self.ui.lineEdit_maTacGia.text().strip()
        tenTacGia = self.ui.lineEdit_tenTacGia.text().strip()
        check = db.handleSuaTacGia(maTacGia, tenTacGia)
        self.handleLoadTacGia_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa tác giả thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa tác giả thất bại')
#EDIT THE LOAI        
    def handleEditTheLoai(self):
        db=mydb()
        msg = QMessageBox()
        maTheLoai = self.ui.lineEdit_maTheLoai.text().strip()
        tenTheLoai = self.ui.lineEdit_tenTheLoai.text().strip()
        check = db.handleSuaTheLoai(maTheLoai, tenTheLoai)
        self.handleLoadTheLoai_table()
        if check:
            msg.setIcon(QMessageBox.Information)
            msg.information(self,'Success', 'Sửa thể loại thành công')
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.information(self,'Failed', 'Sửa thể loại thất bại')
#DELETE NXB        
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
#DELETE TAC GIA            
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
#DELETE THE LOAI            
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
#SEARCH NXB           
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
#SEARCH TAC GIA          
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
#SEARCH THE LOAI            
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