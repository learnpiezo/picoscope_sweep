# -*- coding: utf-8 -*-
"""
Created on Thu May 04 17:29:43 2017

@author: Husain
"""

"""Section 1- create .py from .ui"""
import os
os.system('pyuic4 picoscope_ui.ui > picoscope_ui.py')
from time import sleep #perform delay
sleep(2)

"""Section 2 - Package import"""
import csv
import numpy as np
#import visa
import sys
#from time import gmtime, strftime
import functions as fn # custom functions

"""Section 3 - GUI import"""

from PyQt4 import QtCore, QtGui, uic
from PyQt4 import *
from PyQt4 import QtGui, uic
import sys
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from picoscope_ui import Ui_MainWindow # change the file name

##-------------------------##
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
ui = Ui_MainWindow()
ui.setupUi(window)
##-------------------------##


""" Section 4 - define button functions """
def start():
    #Define frequency iteration values
    startFrequency = ui.startFreq_input.text()
    startFrequency = float(startFrequency)
    endFrequency = ui.stopFreq_input.text()
    endFrequency = float(endFrequency)
    intervalFrequency = ui.intFreq_input.text()
    intervalFrequency = float(intervalFrequency)
    intervals = (endFrequency-startFrequency)/intervalFrequency + 1
    
    #Define frequency array
    frequencySpace = np.linspace(startFrequency,endFrequency,intervals)
    
    #Initialize output measurements
    ch1Voltage = np.linspace(startFrequency,endFrequency,intervals)
    ch2Voltage = np.linspace(startFrequency,endFrequency,intervals)
    impedance = np.linspace(startFrequency,endFrequency,intervals)
    
    # Iterate over frequencySpace and get meeasurements
    for n in range(0,len(frequencySpace)):
        fn.signalGenerator(2,frequencySpace[n])  # set the function generator
        fn.timeBase(frequencySpace[n]) # set the time base
        ch1Voltage[n] , ch2Voltage[n] = fn.getMeasurements() # assign measurement
        impedance[n] = ch1Voltage[n] / (ch2Voltage[n]/325.0) # define impedance
    
    # Write the data to a CSV file
    head = "frequency (Hz), Ch1 Voltage, Ch2 Voltage,Impedance"
    filename = ui.fileName.text()    
    np.savetxt(str(filename) + ".csv", np.transpose([frequencySpace,ch1Voltage,ch2Voltage,impedance]), delimiter=',', header=head)
    
    
    # Plot data from python
    ui.matplotlibwidget.axes.plot(frequencySpace,1/impedance)
    ui.matplotlibwidget.draw() 
    
""" Section 5 - GUI button link """
ui.startButton.clicked.connect(start)

    
""" Section 6 -  exit program """
sys.exit(app.exec_())

