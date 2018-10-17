# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:35:33 2018

@author: sanjio.durasevic
"""

import DyMat
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def dy_mat_func(file):
    
    #for n in f.names():
    #    print(n)
    
    f = DyMat.DyMatFile(file + ".mat")

    time = f.abscissa('HC_B9.T', valuesOnly=True)
    B9_T = f.data('HC_B9.T')-273.15
    A7_T = f.data('HC_A7.T')-273.15
    A2_T = f.data('HC_A2.T')-273.15
    A11_T = f.data('HC_A11.T')-273.15
    B3_T = f.data('HC_B3.T')-273.15

    fi = f.data('fluid_inlet.y')
    fo = f.data('fluid_outlet.y')

    list1 = time.tolist()
    list2 = B9_T.tolist()
    list3 = A7_T.tolist()
    list4 = A2_T.tolist()
    list5 = A11_T.tolist()
    list6 = B3_T.tolist()

    list7 = fi.tolist()
    list8 = fo.tolist()

    data1 = pd.DataFrame({'time': list1, 'T$_{B9}$': list2, 'T$_{A7}$': list3,
                          'T$_{A2}$': list4, 'T$_{A11}$': list5, 'T$_{B3}$': list6})

    data2 = pd.DataFrame({'time': list1, 'T$_{fluid\; inlet}$': list7, 'T$_{fluid\; outlet}$': list8})


    #fig, ax = plt.subplots()
    
    data1.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature $[^{\circ}C]$")
    plt.xlim((0,200))
    plt.ylim((25,135))
    plt.grid(True)
    plt.savefig(file + "_Module_T.png")
    plt.show()
    
    data2.plot(x='time')
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature $[^{\circ}C]$")
    plt.xlim((0,200))
    plt.ylim((20,120))
    plt.grid(True)
    plt.savefig(file + "_HE_T.png")
    plt.show()


file_list = ['ALL_oldCoeffs', 'ALL_newCoeffs']

for file in file_list:
    dy_mat_func(file)