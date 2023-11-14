from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QMargins
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice, QChartView

import sys
from collections import namedtuple

Data = namedtuple('Data', ['name', 'value', 'color'])
class SmartChart(QChart):
    """
    A slightly smarter implementation of pie chart in Qt, with
    double looped pie chart layout design and hover animation.
    """

    def __init__(self, parent=None):
        """
        Initialization with layout and population
        """
        super(SmartChart, self).__init__(parent)
        self.offset = 140

        self.setMargins(QMargins(0, 0, 0, 0))
        self.legend().hide()
        self.setAnimationOptions(QChart.SeriesAnimations)

        self.__outer = QPieSeries()
        self.__inner = QPieSeries()
        self.__outer.setHoleSize(0.35)
        self.__outer.setPieStartAngle(self.offset)
        self.__outer.setPieEndAngle(self.offset+360)
        self.__inner.setPieSize(0.35)
        self.__inner.setHoleSize(0.3)
        self.__inner.setPieStartAngle(self.offset)
        self.__inner.setPieEndAngle(self.offset+360)

        self.addSeries(self.__outer)
        self.addSeries(self.__inner)

    def clear(self):
        """
        Clear all slices in the pie chart
        """
        for slice_ in self.__outer.slices():
            self.__outer.take(slice_)

        for slice_ in self.__inner.slices():
            self.__inner.take(slice_)

    def add_slice(self, name, value, color):
        """
        Add one slice to the pie chart

        :param name: str. name of the slice
        :param value: value. value of the slice (contribute to how much the
                      slice would span in angle)
        :param color: str. hex code for slice color
        """
        # outer
        outer_slice = QPieSlice(name, value)
        outer_slice.setColor(QColor(color))
        outer_slice.setLabelBrush(QColor(color))

        outer_slice.hovered.connect(lambda is_hovered: self.__explode(outer_slice, is_hovered))
        outer_slice.percentageChanged.connect(lambda: self.__update_label(outer_slice, name))

        self.__outer.append(outer_slice)

        # inner
        inner_color = self.__get_secondary_color(color)
        inner_slice = QPieSlice(name, value)
        self.__inner.append(inner_slice)
        inner_slice.setColor(inner_color)
        inner_slice.setBorderColor(inner_color)

    @staticmethod
    def __update_label(slice_, title):
        """
        Update the label of a slice

        :param slice_: QPieSlice. the slice the label is applied
        :param title: str. title of the label
        """
        text_color = 'black'
        if slice_.percentage() > 0.1:
            slice_.setLabelPosition(QPieSlice.LabelInsideHorizontal)
            text_color = 'white'

        label = "<p align='center' style='color:{}'>{}<br>{}%</p>".format(
            text_color,
            title,
            round(slice_.percentage()*100, 2)
            )
        slice_.setLabel(label)

        if slice_.percentage() > 0.03:
            slice_.setLabelVisible()

    def __explode(self, slice_, is_hovered):
        """
        Explode function slot for hovering effect

        :param slice_: QPieSlice. the slice hovered
        :param is_hovered: bool. hover enter (True) or leave (False)
        """
        if is_hovered:
            start = slice_.startAngle()
            end = slice_.startAngle() + slice_.angleSpan()
            self.__inner.setPieStartAngle(end)
            self.__inner.setPieEndAngle(start+360)
        else:
            self.__inner.setPieStartAngle(self.offset)
            self.__inner.setPieEndAngle(self.offset+360)

        slice_.setLabelVisible(is_hovered)
        slice_.setExplodeDistanceFactor(0.1)
        slice_.setExploded(is_hovered)

        if slice_.percentage() > 0.03:
            slice_.setLabelVisible()

    @staticmethod
    def __get_secondary_color(hexcode):
        """
        Get secondary color which is blended 50% with white
        to appear lighter

        :param hexcode: str. color hex code starting with '#'
                        eg. ('#666666')
        :return: QColor
        """
        hexcode = hexcode.lstrip("#")
        color = tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4))
        red, green, blue = color
        return QColor(red, green, blue)


class SimpleChartView(QChartView):
    """
    A simple wrapper chart view, to be expanded
    """
    def __init__(self, chart):
        super(SimpleChartView, self).__init__(chart)

        self.setRenderHint(QPainter.Antialiasing)
