from PyQt5.QtWidgets import QWidget
from chart.Ui_statistic import Ui_Statistic
from chart.piechart import SmartChart, SimpleChartView
from chart.lineChart import LineChart, LineChartView
from connector.mySql import mydb
class statistic(QWidget):
    def __init__(self, logged_in_user):
        super(statistic, self).__init__()
        self.ui = Ui_Statistic()
        self.ui.setupUi(self)
        self.madocgia = logged_in_user
        #self.ui.year_combo_box.addItem("Select Year")  # Placeholder item
        for year in range(2023, 1900, -1):  # You can adjust the range based on your requirements
            self.ui.year_combo_box.addItem(str(year))
        #self.ui.month_combo_box.addItem("Select Month")  # Placeholder item
        for month in range(1, 13):  # You can adjust the range based on your requirements
            self.ui.month_combo_box.addItem(str(month))
        self.ui.month_combo_box.setCurrentText('10')
        
        self.pieChart = SmartChart()
        self.pieChart.resize(700, 400)
        self.pie_chart_view = SimpleChartView(self.pieChart)
        self.ui.gridLayout_pie.addWidget(self.pie_chart_view, 1,0,1,1)
        self.color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
                        "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5",
                        "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
                        "#393b79", "#637939", "#8c6d31", "#843c39", "#7b4173",
                        "#5254a3", "#637939", "#396ab1", "#dd8452", "#7b4173"]
        self.loadCountTheloai()
        self.ui.pieChart_combo_box.addItem("Thống kê sách theo thể loại")  # Placeholder item
        self.ui.pieChart_combo_box.addItem("Thống kê sách theo tác giả")  # Placeholder item
        self.ui.pieChart_combo_box.addItem("Thống kê sách theo nxb")  # Placeholder item
        self.ui.pieChart_combo_box.currentIndexChanged.connect(self.updatePieChart)
        self.thang = self.ui.month_combo_box.currentText()
        self.nam = self.ui.year_combo_box.currentText()
        self.lineChart = LineChart(self.thang, self.nam)
        self.lineChart.resize(700, 400)
        self.lineChartView = LineChartView(self.lineChart)
        self.ui.gridLayout_Line.addWidget(self.lineChartView, 1, 0, 1, 2)    
        self.ui.year_combo_box.currentIndexChanged.connect(self.updateLineChart)
        self.ui.month_combo_box.currentIndexChanged.connect(self.updateLineChart)
    
    def updateLineChart(self, ):
        # Get the selected values from the combo boxes
        selected_year = self.ui.year_combo_box.currentText()
        selected_month = self.ui.month_combo_box.currentText()

        # Update the line chart based on the selected values
        self.lineChart.update(selected_month, selected_year)

    
    def updatePieChart(self, index):
        if(index == 0):
            self.loadCountTheloai()
        elif(index == 1):
            self.loadCountTacGia()
        else:
            self.loadCountNXB()
        
    def loadCountTheloai(self):
        db = mydb()
        results = db.loadCountLoai()
        self.pieChart.clear()
        i=0
        for record in results:
            self.pieChart.add_slice(record[1], record[2], self.color[i])
            i+=1
    
    def loadCountTacGia(self):
        db = mydb()
        results = db.loadCountTacGia()
        self.pieChart.clear()
        i=0
        for record in results:
            self.pieChart.add_slice(record[1], record[2], self.color[i])
            i+=1
            
    def loadCountNXB(self):
        db = mydb()
        results = db.loadCountNXB()
        self.pieChart.clear()
        i=0
        for record in results:
            self.pieChart.add_slice(record[1], record[2], self.color[i])
            i+=1        