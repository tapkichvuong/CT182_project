from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF
from connector.mySql import mydb

class LineChart(QChart):
    def __init__(self, thang, nam):
        super(LineChart, self).__init__()
        self.borrowSeries = QLineSeries()
        self.thang = thang
        self.nam = nam
        self.handleLoadBorrowFlow()
        self.addSeries(self.borrowSeries)
        self.createDefaultAxes()
        self.setTitle("Lượng sách được mượn trong 1 tháng")
        
        axis_x = QValueAxis()
        axis_x.setTickCount(5)  # Number of tick intervals
        axis_x.setLabelFormat("%d")  # Format of the labels
        axis_x.setRange(1, 31)  # Range of x-axis values
        axis_x.setTickCount(5)  # Number of tick intervals
        axis_x.setTitleText("Ngày")  # Set X-axis label
        self.setAxisX(axis_x, self.borrowSeries)
        
        axis_y = QValueAxis()
        axis_y.setTickCount(5)  # Number of tick intervals
        axis_y.setLabelFormat("%d")  # Format of the labels
        axis_y.setRange(1, 15)  # Range of x-axis values
        axis_y.setTickCount(5)  # Number of tick intervals
        axis_y.setTitleText("Quyển")  # Set X-axis label
        self.setAxisY(axis_y, self.borrowSeries)
        self.legend().hide()
        
    def handleLoadBorrowFlow(self):
        db = mydb()
        results = db.handleLoadBorrowFlow(self.thang, self.nam)
        print(self.thang, self.nam)
        print(results)
        for result in results:
            self.borrowSeries.append(result[0], result[1])
    
    def update(self, thang, nam):
        db = mydb()
        results = db.handleLoadBorrowFlow(thang, nam)
        print(results)
        self.borrowSeries.clear()
        for result in results:
            self.borrowSeries.append(result[0], result[1])
          
class LineChartView(QChartView):
    def __init__(self, chart):
        super(LineChartView, self).__init__(chart)
        self.setRenderHint(QPainter.Antialiasing)
