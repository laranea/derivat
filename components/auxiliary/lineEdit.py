# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:39:53 2016

@author: Ryan
"""

import PyQt4.QtCore as Qt
import PyQt4.QtGui as QtGui

class CustomLineEdit(QtGui.QWidget):
    changedSignal = Qt.pyqtSignal(object)
    def __init__(self, default_text, parent = None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QHBoxLayout() 
        layout.setAlignment(Qt.Qt.AlignTop)
        self.line_edit = self.addLineEdit(layout, default_text)
        self.setLayout(layout)
        self.link() 
    def addLineEdit(self, layout, default_text):
        line_edit = QtGui.QLineEdit()
        if default_text:
            line_edit.setText(str(default_text).upper())
        layout.addWidget(line_edit)
        return line_edit

class AutoUpperLineEdit(CustomLineEdit):
    def __init__(self, default_text):
        super(AutoUpperLineEdit, self).__init__(default_text)
    def link(self):
        self.line_edit.textChanged.connect(self.capitalize)
    def capitalize(self):
        self.line_edit.setText(str(self.line_edit.text()).upper())
        self.changedSignal.emit(self.text())
        Qt.QCoreApplication.processEvents()
    def text(self):
        return self.line_edit.text()
        
class AutoNumeralLineEdit(CustomLineEdit):
    def __init__(self, default_text = ''):
        super(AutoNumeralLineEdit, self).__init__(default_text)
    def link(self):
        self.line_edit.textChanged.connect(self.checkNumeral)
    def checkNumeral(self):
        self.line_edit.setText(filter( lambda x: x in '0123456789.+-', str(self.line_edit.text()) ))
        self.changedSignal.emit(self.value())
        Qt.QCoreApplication.processEvents()
    def value(self):
        return float(self.line_edit.text())
        
class ListNumeralsLineEdit(CustomLineEdit):
    def __init__(self, default_text = None):
        super(ListNumeralsLineEdit, self).__init__(default_text)
    def link(self):
        self.line_edit.textChanged.connect(self.checkNumericList)
    def checkNumericList(self):
        text = filter(lambda x: x in '0123456789.,', str(self.line_edit.text()))
        self.line_edit.setText(', '.join(text.split(',')))
        self.changedSignal.emit(self.value())
        Qt.QCoreApplication.processEvents()
    def value(self):
        ret = []
        for num in filter(lambda x: x in '0123456789.,', str(self.line_edit.text())).split(','):
            ret.append(num)
        return num