from typing import List
import pandas as pd 
import numpy as np 
import matplotlib as mpl
mpl.use('macosx')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import statistics as stats
import pylab
#import plotly.graph_objects as go
def plotter(filenames):
    raw1=np.loadtxt(filenames[0],delimiter='\t',skiprows=4)
    raw2=np.loadtxt(filenames[1],delimiter='\t',skiprows=4)
    raw3=np.loadtxt(filenames[2],delimiter='\t',skiprows=4)
    raw4=np.loadtxt(filenames[3],delimiter='\t',skiprows=4)
    R1=raw1.T
    R2=raw2.T
    R3=raw3.T
    R4=raw4.T
    
    #---------------------Intilising 1-----------------------#
    x1,y1 = raw1.shape
    COMPNUM=y1-5
    NR1 = []
    for i in range(0,y1):
        if i<=1:
            NR1.append(R1[i])
        if i>=2:
            NR1.append((R1[i])/max(R1[2]))
    
    #---------------------Intilising 2-----------------------#
    x2,y2 = raw2.shape
    COMPNUM2=y2-5
    NR2 = []
    s2=.05
    for i in range(0,y2):
        
        if i<=1:
            NR2.append(R2[i])
        if i>=2:
            NR2.append((R2[i])/max(R2[2])+s2)
    
    #---------------------Intilising 3-----------------------#
    x3,y3 = raw3.shape
    COMPNUM2=y3-5
    NR3 = []
    s3=.05
    for i in range(0,y3):
        if i<=1:
            NR3.append(R3[i])
        if i>=2:
            NR3.append((R3[i])/max(R3[2])+s2+s3)
    #---------------------Intilising 4-----------------------#
    x4,y4 = raw4.shape
    COMPNUM4=y4-5
    NR4 = []
    s4=.05
    for i in range(0,y4):
        
        if i<=1:
            NR4.append(R4[i])
        if i>=2:
            NR4.append((R4[i])/max(R4[2])+s2+s3+s4)
    #------------------------Plotting-------------------------#
    fig1 = plt.figure(figsize=(8,8))
    ax = fig1.add_subplot(111)
    ax.set_xlabel('Binding Energy (eV)',fontname="Times")
    plt.scatter(NR1[1],NR1[2],color = [1,0,0])
    for i in range(0,COMPNUM):
        plt.plot(NR1[1],NR1[3+i])
    plt.plot(NR1[1],NR1[-1])
    plt.plot(NR1[1],NR1[-2])
    #--2nd plot--#
    plt.scatter(NR2[1],NR2[2])
    plt.plot(NR2[1],NR2[-1])
    #--3rd plot--#
    plt.scatter(NR3[1],NR3[2])
    plt.plot(NR3[1],NR3[-1])
    #--4th plot--#
    plt.scatter(NR4[1],NR4[2])
    plt.plot(NR4[1],NR4[-1])
    
    
    #Fiddling with plot properties
    pylab.xlim([528,540])
    plt.gca().invert_xaxis()
    ax.yaxis.set_ticks_position('none')
    ax.set_yticklabels([])
    ax.set_ylabel('Intensity (arb. units.)',fontname="Times")
    
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(20)
    plt.xticks(fontname = "Times")
    
    plt.show()
    
def main():
    O1s=['Etching/o-100-1.TXT',    
         'Etching/o-100-2.TXT',
         'Etching/o-100-2.TXT',
         'Etching/o-100-2.TXT']
    O1scol=[]
    plotter(O1s)
main()
