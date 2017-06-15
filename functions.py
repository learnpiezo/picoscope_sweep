# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:37:43 2017

@author: Husain
"""
import subprocess

def getMeasurements():
    #read oscilloscope
    output = subprocess.check_output(['picoscope','/a','Measurements.CSV?'])    
    #split the lines of the measurements    
    output = output.split('\n')
    #define space
    space = " "
    #taking the index, and splitting according to comma
    channelA = output[1].split(",")
    channelB = output[2].split(",")
    #taking index, and splitting according to "space"
    channelA = channelA[2].split(space)    
    channelB = channelB[2].split(space)    
    #check the unit and apply    
    if channelA[1]=="mV":
        channelA=float(channelA[0])*1E-3
    elif channelA[1]=="V":
        channelA=float(channelA[0])*1
    else:
        channelA=float(channelA[0])*1E-6
    
    if channelB[1]=="mV":
        channelB=float(channelB[0])*1E-3
    elif channelB[1]=="V":
        channelB=float(channelB[0])*1
    else:
        channelB=float(channelB[0])*1E-6    
    
    return [channelA,channelB]

def signalGenerator(amp,freq):
    #define input strings to input to cmd line
    amp_string = "picoscope /a Siggen.Amplitude.Value="+str(amp)
    freq_string = "picoscope /a Siggen.Frequency.Value="+str(freq)
    subprocess.call(amp_string,stdout=False)
    subprocess.call(freq_string,stdout=False)
    
def timeBase(freq):    
    #find ideal timebase
    time_base=1/float(freq)*5/10
    #define time_index corellations
    time_index = [200E-9,500E-9,1E-6,2E-6,5E-6,10E-6,20E-6,50E-6,100E-6,200E-6,500E-6,1E-3,2E-3,5E-3,10E-3,20E-3,50E-3,100E-3]
    #find time index for command line    
    for n in range(0,len(time_index)):
        if time_base<time_index[n]:
            break
    #write string to command line to change timebase
    time_base_string = "picoscope /a CollectionTime.SelectedIndex="+str(n+1)
    subprocess.call(time_base_string,stdout=False)

# define the frequency array

"""
import numpy as np

#Define frequency iteration values
startFrequency = 39000
endFrequency = 41000
intervalFrequency = 10
intervals = (endFrequency-startFrequency)/intervalFrequency + 1

#Define frequency array
frequencySpace = np.linspace(startFrequency,endFrequency,intervals)

#Initialize output measurements
ch1Voltage = np.linspace(startFrequency,endFrequency,intervals)
ch2Voltage = np.linspace(startFrequency,endFrequency,intervals)
impedance = np.linspace(startFrequency,endFrequency,intervals)

# Iterate over frequencySpace and get meeasurements
for n in range(0,len(frequencySpace)):
    signalGenerator(2,frequencySpace[n])  # set the function generator
    timeBase(frequencySpace[n]) # set the time base
    ch1Voltage[n] , ch2Voltage[n] = getMeasurements() # assign measurement
    impedance[n] = ch1Voltage[n] / (ch2Voltage[n]/325.0) # define impedance

# Write the data to a CSV file
head = "frequency (Hz), Ch1 Voltage, Ch2 Voltage,Impedance"
np.savetxt("10kHzTO50kHzS100Hz.csv", np.transpose([frequencySpace,ch1Voltage,ch2Voltage,impedance]), delimiter=',', header=head)


# Plot data from python
import matplotlib.pyplot as plt
plt.plot(frequencySpace,impedance)
plt.yscale('log')
plt.show()


#signalGenerator(0.2,80222)
#timeBase(80222)   
  
#print getMeasurements()
#signalGenerator(1.32,50E3)
"""
