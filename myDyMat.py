# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:35:33 2018

@author: sanijo.durasevic
"""

import sys
import DyMat as dm
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


files_list = ['0-300_oldCoeff_k_0.8', '0-300_oldCoeff_k_1.2']

def dy_mat_func(file):
    
    #for n in f.names():
    #    print(n)
    
    f = dm.DyMatFile(file + ".mat")
    
    #Stores values from .mat file to numpy array
    time = f.abscissa('HC_B9.T', valuesOnly=True)
    B9_T = f.data('HC_B9.T')-273.15
    A7_T = f.data('HC_A7.T')-273.15
    A2_T = f.data('HC_A2.T')-273.15
    A11_T = f.data('HC_A11.T')-273.15
    B3_T = f.data('HC_B3.T')-273.15
    
    #speed
    v = f.data('Speed.y[1]')
    
    #Perscribed heat flow (conversion from W to kW)
    Q = f.data('timeTable.y[1]')/1000
    
    #Inlet and outlet temperature of HE or Radiator
    fi = f.data('fluid_inlet.y')
    fo = f.data('fluid_outlet.y')
    
    #Conversion of arrays to lists
    list1 = time.tolist()
    list2 = B9_T.tolist()
    list3 = A7_T.tolist()
    list4 = A2_T.tolist()
    list5 = A11_T.tolist()
    list6 = B3_T.tolist()

    list7 = fi.tolist()
    list8 = fo.tolist()
    
    list9 = v.tolist()
    list10 = Q.tolist()
    
    #Dataframes for plotting
    data1 = pd.DataFrame({'time': list1, 'T$_{B9}$': list2, 'T$_{A7}$': list3,
                          'T$_{A2}$': list4, 'T$_{A11}$': list5, 'T$_{B3}$': list6})

    data2 = pd.DataFrame({'time': list1, 'T$_{fluid\; inlet}$': list7, 'T$_{fluid\; outlet}$': list8})
    
    data3 = pd.DataFrame({'time': list1, 'Velocity [km/h]': list9})
    
    data4 = pd.DataFrame({'time': list1, 'Q [kW]': list10})

    #fig, ax = plt.subplots()
    
    data1.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature $[^{\circ}C]$")
    #plt.xlim((0,694))
    #plt.ylim((25,120))
    plt.autoscale(tight=True)
    plt.grid(True)
    plt.title(file)
    plt.savefig(file + "_Module_T.png")
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
    plt.legend().remove()
    plt.savefig(file + "_Q.png")
    plt.show()
    
    #All plots
    f, axarr = plt.subplots(2, 2, figsize=(14, 10))
    
    axarr[0, 0].plot(list1, list2, label='T$_{B9}$')
    axarr[0, 0].plot(list1, list3, label='T$_{A7}$')
    axarr[0, 0].plot(list1, list4, label='T$_{A2}$')
    axarr[0, 0].plot(list1, list5, label='T$_{A11}$')
    axarr[0, 0].plot(list1, list6, label='T$_{B3}$')
    axarr[0, 0].set_xlabel("Time [s]", fontsize=10)
    axarr[0, 0].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0, 0].autoscale(tight=True)
    axarr[0, 0].grid(True)
    axarr[0, 0].legend()
    #axarr[0, 0].set_title(file)
    
    axarr[0, 1].plot(list1, list7, label='T$_{fluid\; inlet}$')
    axarr[0, 1].plot(list1, list8, label='T$_{fluid\; outlet}$')
    axarr[0, 1].set_xlabel("Time [s]", fontsize=10)
    axarr[0, 1].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0, 1].autoscale(tight=True)
    axarr[0, 1].grid(True)
    axarr[0, 1].legend()
    #axarr[0, 1].set_title(file)
    
    axarr[1, 0].plot(list1, list9)
    axarr[1, 0].set_xlabel("Time [s]", fontsize=10)
    axarr[1, 0].set_ylabel("Velocity [km/h]", fontsize=10)
    axarr[1, 0].autoscale(tight=True)
    axarr[1, 0].grid(True)
    #axarr[1, 0].set_title(file)
    
    axarr[1, 1].plot(list1, list10)  
    axarr[1, 1].set_xlabel("Time [s]", fontsize=10)
    axarr[1, 1].set_ylabel("Q [kW]", fontsize=10)
    axarr[1, 1].autoscale(tight=True)
    axarr[1, 1].grid(True)
    #axarr[1, 1].set_title(file)
    
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.suptitle(file)
    plt.savefig(file + "_COMPLETE.pdf", format='pdf')
    plt.show()

for file in files_list:
    dy_mat_func(file)