# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:21:15 2018

@author: sanijo.durasevic
"""

import sys
import DyMat as dm
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


#files_list = ['Nardo_handling_w_25deg', 'Nardo_handling_w_40deg', 'Nardo_handling_wo_25deg', 'Nardo_handling_wo_40deg',
#              'Nardo_oval1_25deg', 'Nardo_oval1_40deg', 'Nurburgring_w_25deg', 'Nurburgring_w_40deg', 'Nurburgring_wo_25deg',
#              'Nurburgring_wo_40deg']

files_list = ['Nardo_handling_w_25deg']

def averageQ(list):
    
    counter = 0
    sum = 0
    for q in list:
        sum += q
        counter += 1
    avg = sum / counter
    Q_avg = np.linspace(avg, avg, counter)
    
    return(Q_avg.tolist()) 

def dy_mat_func(file):
    
    #for n in f.names():
    #    print(n)
    
    f = dm.DyMatFile(file + ".mat")
    
    #Stores values from .mat file to numpy array
    time = f.abscissa('MotorLeft.T', valuesOnly=True)
    MotorL = f.data('MotorLeft.T')-273.15
    MotorR = f.data('MotorRight.T')-273.15
       
    #speed
    v = f.data('Speed.y[1]')
    
    #Perscribed heat flow (conversion from W to kW)
    Q_L = f.data('timeTable1.y[1]')/1000
    Q_R = f.data('timeTable2.y[1]')/1000
    
    #Inlet and outlet temperature of HE or Radiator
    fi = f.data('HE_inlet1.y')
    fo = f.data('HE_outlet1.y')
    
    #Conversion of arrays to lists
    list1 = time.tolist()
    list2 = MotorL.tolist()
    list3 = MotorR.tolist()

    list4 = fi.tolist()
    list5 = fo.tolist()
    
    list6 = v.tolist()
    list7 = Q_L.tolist()
    list8 = Q_R.tolist()
    
    #Average heat flow
    list9 = averageQ(list7)   
    list10 = averageQ(list8)


    #Dataframes for plotting
    data1 = pd.DataFrame({'time': list1, 'T$_{left\; motor}$': list2, 'T$_{right\; motor}$': list3})

    data2 = pd.DataFrame({'time': list1, 'T$_{fluid\; inlet}$': list4, 'T$_{fluid\; outlet}$': list5})
    
    data3 = pd.DataFrame({'time': list1, 'Velocity [km/h]': list6})
    
    data4 = pd.DataFrame({'time': list1, 'Q$_{left\; motor}$ [kW]': list7, 'Q$_{right\; motor}$ [kW]': list8,
                          'Q$_{average\; left}$ [kW]': list9, 'Q$_{average\; right}$ [kW]': list10})

    #fig, ax = plt.subplots()
    
    data1.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature $[^{\circ}C]$")
    #plt.xlim((0,694))
    #plt.ylim((25,120))
    plt.autoscale(tight=True)
    plt.grid(True)
    plt.title(file)
    plt.savefig(file + "_Motor_T.png")
    plt.show()
    
    data2.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature $[^{\circ}C]$")
    plt.autoscale(tight=True)
    #plt.xlim((0,694))
    #plt.ylim((20,100))
    plt.grid(True)
    plt.title(file)
    plt.savefig(file + "_HE_T.png")
    plt.show()
    
    data3.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [km/h]")
    plt.autoscale(tight=True)
    #plt.xlim((0,694))
    #plt.ylim((0,100))
    plt.grid(True)
    plt.title(file)
    plt.legend().remove()
    plt.savefig(file + "_velocity.png")
    plt.show()
    
    data4.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Q [kW]")
    #plt.xlim((0,694))
    #plt.ylim((0,25))
    plt.autoscale(tight=True)
    plt.grid(True)
    plt.title(file)
    #plt.legend().remove()
    plt.savefig(file + "_Q.png")
    plt.show()
    
    #All plots
    f, axarr = plt.subplots(2, 2, figsize=(14, 10))
    
    axarr[0, 0].plot(list1, list2, label='T$_{left\; motor}$')
    axarr[0, 0].plot(list1, list3, label='T$_{right\; motor}$')
    axarr[0, 0].set_xlabel("Time [s]", fontsize=10)
    axarr[0, 0].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0, 0].autoscale(tight=True)
    axarr[0, 0].grid(True)
    axarr[0, 0].legend()
    #axarr[0, 0].set_title(file)
    
    axarr[0, 1].plot(list1, list4, label='T$_{fluid\; inlet}$')
    axarr[0, 1].plot(list1, list5, label='T$_{fluid\; outlet}$')
    axarr[0, 1].set_xlabel("Time [s]", fontsize=10)
    axarr[0, 1].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0, 1].autoscale(tight=True)
    axarr[0, 1].grid(True)
    axarr[0, 1].legend()
    #axarr[0, 1].set_title(file)
    
    axarr[1, 0].plot(list1, list6)
    axarr[1, 0].set_xlabel("Time [s]", fontsize=10)
    axarr[1, 0].set_ylabel("Velocity [km/h]", fontsize=10)
    axarr[1, 0].autoscale(tight=True)
    axarr[1, 0].grid(True)
    #axarr[1, 0].set_title(file)
    
    axarr[1, 1].plot(list1, list7, label='Q$_{left\; motor}$ [kW]') 
    axarr[1, 1].plot(list1, list8, label='Q$_{right\; motor}$ [kW]')
    axarr[1, 1].plot(list1, list9, label='Q$_{average\; left}$ [kW]')
    axarr[1, 1].plot(list1, list10, label='Q$_{average\; right}$ [kW]')
    axarr[1, 1].set_xlabel("Time [s]", fontsize=10)
    axarr[1, 1].set_ylabel("Q [kW]", fontsize=10)
    axarr[1, 1].autoscale(tight=True)
    axarr[1, 1].grid(True)
    axarr[1, 1].legend()
    #axarr[1, 1].set_title(file)
    
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.suptitle(file)
    plt.savefig(file + "_COMPLETE.png", format='png')
    plt.show()

for file in files_list:
    dy_mat_func(file)