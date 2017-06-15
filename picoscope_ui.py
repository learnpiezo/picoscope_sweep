# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picoscope_ui.ui'
#
# Created: Wed May 31 15:26:37 2017
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(467, 457)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.fileName = QtGui.QLineEdit(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(280, 20, 161, 20))
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.startFreq_input = QtGui.QLineEdit(self.centralwidget)
        self.startFreq_input.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.startFreq_input.setObjectName(_fromUtf8("startFreq_input"))
        self.stopFreq_input = QtGui.QLineEdit(self.centralwidget)
        self.stopFreq_input.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.stopFreq_input.setObjectName(_fromUtf8("stopFreq_input"))
        self.intFreq_input = QtGui.QLineEdit(self.centralwidget)
        self.intFreq_input.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.intFreq_input.setObjectName(_fromUtf8("intFreq_input"))
        self.matplotlibwidget = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget.setGeometry(QtCore.QRect(40, 120, 400, 300))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.fileName.setText(_translate("MainWindow", "filename", None))
        self.label.setText(_translate("MainWindow", "start frequency", None))
        self.label_2.setText(_translate("MainWindow", "stop frequency", None))
        self.label_3.setText(_translate("MainWindow", "int frequency", None))
        self.startFreq_input.setText(_translate("MainWindow", "1000", None))
        self.stopFreq_input.setText(_translate("MainWindow", "70000", None))
        self.intFreq_input.setText(_translate("MainWindow", "1000", None))
        self.startButton.setText(_translate("MainWindow", "start", None))

from matplotlibwidget import MatplotlibWidget
