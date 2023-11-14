import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from mainwindow.Ui_sidebar import Ui_MainWindow
from qlSach.qlSach import qlsach
from ql_tp_sach.ql_tp_sach import ql_tp_sach
from changePassword.changePassword import change_password
from myProfile.profile import profile
from muontra.muontra import ql_muontra
from chart.Statistic import statistic
from connector.mySql import mydb

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

        
        self.ql_muontra = ql_muontra()
        self.ui.gridLayout_5.addWidget(self.ql_muontra,0,0,1,1)
        
        
        self.ql_tp = ql_tp_sach()
        self.ui.gridLayout_9.addWidget(self.ql_tp, 0,0,1,1)
        
        self.change_pass_page = change_password(self.logged_in_user)
        self.ui.gridLayout_8.addWidget(self.change_pass_page, 0,0,1,1)
        
        self.profile = profile(self.logged_in_user)
        self.ui.gridLayout_6.addWidget(self.profile, 0,0,1,1)
        
        self.statistic = statistic(self.logged_in_user)
        self.ui.gridLayout_3.addWidget(self.statistic, 0,0,1,1)
        
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
    
    # def on_home_btn_2_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(0)

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



