
import PyQt4.QtCore as Qt
import PyQt4.QtGui as QtGui

class AutoAxisTable(QtGui.QTableWidget):
    def __init__(self, row_labels, column_labels, parent = None):
        QtGui.QTableWidget.__init__(self, parent)
        self.setRowCount(len(row_labels) + 1)
        self.setColumnCount(len(column_labels) + 1)
        
    def updateRowLabels(self, labels):
        self.setRowCount(len(labels))
        for i in range(len(labels)):
            self.setItem(1 + i, 0, QtGui.QTableWidgetItem(str(labels[i])))

    def updateColumnLabels(self, labels):
        self.setColumnCount(len(labels))
        for i in range(len(labels)):
            self.setItem(0, 1 + i , QtGui.QTableWidgetItem(str(labels[i])))



