import psutil
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from .chart import Chart

class MemoryProvider(object):
    delay = 5

    def __init__(self, main_window):
        self.main_window = main_window
        self.label = QtWidgets.QLabel()
        self.chart = Chart(QtCore.QSize(40, main_window.height()))
        main_window[0].right_widget.layout().addWidget(self.label)
        main_window[0].right_widget.layout().addWidget(self.chart)

    def refresh(self):
        self.percentage = psutil.phymem_usage().percent

    def render(self):
        self.label.setText('%.0f%%' % (self.percentage))
        # if self.percentage > 3:
        #     self.label.setProperty('percent', 'high')
        # else:
        #     self.label.setProperty('percent', 'low')
        # self.main_window.reloadStyleSheet()

        self.chart.addPoint('#ff0000', self.percentage)
        self.chart.repaint()
