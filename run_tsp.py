# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:41:43 2018

@author: sanijo.durasevic
"""

from dymola.dymola_interface import DymolaInterface
import os 
import sys
import DyMat as dm
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from datetime import date

today = str(date.today().isoformat())

dir_save = 'C:/Users/sanjio.durasevic/Desktop/TSP/'+today+'_results' 
print(dir_save)
os.makedirs(dir_save, exist_ok=True)

dir_modelon = r'C:\Program Files\Dymola 2018 FD01\Modelica\Library\Modelon 3.2\package.moe'
dir_lcl = r'C:\Program Files\Dymola 2018 FD01\Modelica\Library\LiquidCooling 2.1\package.moe'

path_model1 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Inverter_dc1.mo'
path_model2 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Inverter_dc2.mo'
path_model3 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Inverter_dc3.mo'
path_model4 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Inverter_dc4.mo'
path_model5 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Motor_FINAL_dc1.mo'
path_model6 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Motor_FINAL_dc2.mo'
path_model7 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Motor_FINAL_dc3.mo'
path_model8 = 'C:/Users/sanjio.durasevic/Desktop/TSP/Motor_FINAL_dc4.mo'

paths1 = [path_model1, path_model2, path_model3, path_model4]

models1 = ['Inverter_dc1', 'Inverter_dc2', 'Inverter_dc3', 'Inverter_dc4']

paths2 = [path_model5, path_model6, path_model7, path_model8]

models2 = ['Motor_FINAL_dc1', 'Motor_FINAL_dc2', 'Motor_FINAL_dc3', 'Motor_FINAL_dc4']


times = [775, 790 ,160, 105]

files_list1 = ['Inverter_dc1', 'Inverter_dc2', 'Inverter_dc3', 'Inverter_dc4']
files_list2 = ['Motor_FINAL_dc1', 'Motor_FINAL_dc2', 'Motor_FINAL_dc3', 'Motor_FINAL_dc4']

# Initial values
A_i = 0.064
t_i = 313.15
htc_i = 212
A_m = 0.58
t_m = 313.15
htc_m = 237

def simulation(paths, models, times, A, t, htc, modelon, lcl, dir_save):
    
    modelon = modelon
    lcl = lcl
    A = A
    t = t
    htc = htc
    dir_save = dir_save
    
    for pat, model, time in zip(paths, models, times):
        dymola = None
        try:
            # Instantiate the Dymola interface and start Dymola
            dymola = DymolaInterface()
    
            # Loading libs
            dymola.openModel(path=modelon) 
            dymola.openModel(path=lcl)
    
            # Load model
            dymola.openModel(path=pat)
    
            dymola.translateModel(model)

            # Call a function in Dymola and check its return value
            result = dymola.simulateExtendedModel(problem=model, startTime=0, stopTime=time, outputInterval=0.5,
                                                  method="Esdirk45a", initialNames=["A", "T", "htc"], initialValues=[A, t, htc],
                                                  resultFile=dir_save + "\\" + model)
#            result = dymola.simulateModel("C_Two_M_and_I", startTime=0, stopTime=t_stop, resultFile=dir_path + "_result")
            if not result:
                print("Simulation failed. Below is the translation log.")
                log = dymola.getLastErrorLog()
                print(log)
            
#             dymola.plot(["MotorStator.T", "Inverter_Al.T"], legends=['T_motor', 'T_inverter'])
#             dymola.ExportPlotAsImage(r'C:\Users\sanjio.durasevic\Desktop\C2\12_11_2018_Motor_Inverter_script\plots\slika.png')
        except DymolaException as ex:
            print("Error: " + str(ex))
        finally:
            if dymola is not None:
                dymola.close()
                dymola = None
        

def dy_mat_func_inverter(file):
    
    #for n in f.names():
    #    print(n)
    
    f = dm.DyMatFile(file + ".mat")
    
    #Stores values from .mat file to numpy array
    time = f.abscissa('Chip1.T', valuesOnly=True)
    T1 = f.data('Chip1.T')-273.15
    T2 = f.data('DC.T')-273.15
    T3 = f.data('Housing_1.T')-273.15
    T4 = f.data('Housing_pins.T')-273.15
    T5 = f.data('Vapor_chamber.T')-273.15
    T6 = f.data('Insulation.T')-273.15
    
    #Rejected heat flow [W]
    Q = f.data('volume.q.Q_flow')
  
    #Conversion of arrays to lists
    list1 = time.tolist()
    list2 = T1.tolist()
    list3 = T2.tolist()
    list4 = T3.tolist()
    list5 = T4.tolist()
    list6 = T5.tolist()
    list7 = T6.tolist()
    
    list8 = Q.tolist()
    
    #Dataframes for plotting
    data1 = pd.DataFrame({'time': list1, 'T$_{chip}$': list2, 'T$_{AC/DC\; copper}$': list3,
                          'T$_{housing}$': list4, 'T$_{pins}$': list5, 'T$_{vapor\; chamber}$': list6,
                          'T$_{insulation}$': list7})
    
    data2 = pd.DataFrame({'time': list1, 'Q [W]': list8})
    
    xmin = 0
    xmax = max(list1)
    ymin1 = min(list2)
    ymax1 = max(list2)
    ymin2 = min(list8)
    ymax2 = max(list8)
    
    print("Max temperature for case " + file + ": " + str(round(ymax1, 2)) + " degC.")
    
    with open ("Results.txt", "a") as f:
        f.write("Max temperature for case " + file + ": " + str(round(ymax1, 2)) + " degC.\n")
    
#    data1.plot(x='time')
#    plt.xlabel("Time [s]")
#    plt.ylabel("Temperature $[^{\circ}C]$")
#    plt.xlim(xmin, xmax)
#    plt.ylim(ymin1, ymax1+5)
##    plt.autoscale(tight=True)
#    plt.grid(True)
#    plt.title(file)
#    plt.savefig(file + "_Inverter_T.png")
#    plt.show()
#       
#    data2.plot(x='time')
#    plt.xlabel("Time [s]")
#    plt.ylabel("Q [W]")
#    plt.xlim(xmin, xmax)
#    plt.ylim(ymin2, ymax2+5)
##    plt.autoscale(tight=True)
#    plt.grid(True)
#    plt.title(file)
#    plt.legend().remove()
#    plt.savefig(file + "_Q.png")
#    plt.show()
    
#    #All plots
    f, axarr = plt.subplots(2, sharex=True, figsize=(15, 10))
    
    axarr[0].plot(list1, list2, label='T$_{chip}$')
    axarr[0].plot(list1, list3, label='T$_{AC/DC\; copper}$')
    axarr[0].plot(list1, list4, label='T$_{housing}$')
    axarr[0].plot(list1, list5, label='T$_{pins}$')
    axarr[0].plot(list1, list6, label='T$_{vapor\; chamber}$')
    axarr[0].plot(list1, list7, label='T$_{insulation}$')
    axarr[0].set_xlabel("Time [s]", fontsize=10)
    axarr[0].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0].set_xlim(xmin, xmax) 
    axarr[0].set_ylim(ymin1, ymax1+5) 
#    axarr[0].autoscale(tight=True)
    axarr[0].grid(True)
    axarr[0].legend()
#    plt.xlim((0,694))
#    axarr[0].set_title(file)
    
    axarr[1].plot(list1, list8)
    axarr[1].set_xlabel("Time [s]", fontsize=10)
    axarr[1].set_ylabel("Q [W]", fontsize=10)
    axarr[1].set_xlim(xmin,xmax)
    axarr[1].set_ylim(ymin2, ymax2+5) 
#    axarr[1].autoscale(tight=True)
    axarr[1].grid(True)
#    axarr[1, 0].set_title(file)
    
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.suptitle(file)
    plt.savefig(file + "_complete.png", format='png')
    plt.show()
    
def dy_mat_func_motor(file):
    
    #for n in f.names():
    #    print(n)
    
    f = dm.DyMatFile(file + ".mat")
    
    #Stores values from .mat file to numpy array
    time = f.abscissa('Shaft.T', valuesOnly=True)
    T1 = f.data('Shaft.T')-273.15
    T2 = f.data('Magnet.T')-273.15
    T3 = f.data('Tooth_outerInner.T')-273.15
    T4 = f.data('StatorYoke.T')-273.15
    T5 = f.data('Winding.T')-273.15
    T6 = f.data('Housing_pin.T')-273.15
    T7 = f.data('Housing_casing.T')-273.15
    T8 = f.data('Gearbox.T')-273.15
    
    
    #Rejected heat flow [W]
    Q = f.data('volume.q.Q_flow')
  
    #Conversion of arrays to lists
    list1 = time.tolist()
    list2 = T1.tolist()
    list3 = T2.tolist()
    list4 = T3.tolist()
    list5 = T4.tolist()
    list6 = T5.tolist()
    list7 = T6.tolist()
    list8 = T7.tolist()
    list9 = T8.tolist()
    
    list10 = Q.tolist()
    
    #Dataframes for plotting
    data1 = pd.DataFrame({'time': list1, 'T$_{shaft}$': list2, 'T$_{magnet}$': list3,
                          'T$_{stator\; tooth}$': list4, 'T$_{stator\; yoke}$': list5, 'T$_{winding}$': list6, 
                          'T$_{pins}$': list7, 'T$_{casing}$': list8, 'T$_{gearbox}$': list9})
    
    data2 = pd.DataFrame({'time': list1, 'Q [W]': list10})
    
    xmin = 0
    xmax = max(list1)
    ymin1 = min(list6)
    ymax1 = max(list6)
    ymin2 = min(list10)
    ymax2 = max(list10)
    
    print("Max temperature for case " + file + ": " + str(round(ymax1, 2)) + " degC.")
    
    with open ("Results.txt", "a") as f:
        f.write("Max temperature for case " + file + ": " + str(round(ymax1, 2)) + " degC.\n")
    
    
#    data1.plot(x='time')
#    plt.xlabel("Time [s]")
#    plt.ylabel("Temperature $[^{\circ}C]$")
#    plt.xlim(xmin, xmax)
#    plt.ylim(ymin1, ymax1+5)
##    plt.autoscale(tight=True)
#    plt.grid(True)
#    plt.title(file)
#    plt.savefig(file + "_Inverter_T.png")
#    plt.show()
#       
#    data2.plot(x='time')
#    plt.xlabel("Time [s]")
#    plt.ylabel("Q [W]")
#    plt.xlim(xmin, xmax)
#    plt.ylim(ymin2, ymax2+5)
##    plt.autoscale(tight=True)
#    plt.grid(True)
#    plt.title(file)
#    plt.legend().remove()
#    plt.savefig(file + "_Q.png")
#    plt.show()
    
#    #All plots
    f, axarr = plt.subplots(2, sharex=True, figsize=(15, 10))
    
    axarr[0].plot(list1, list2, label='T$_{shaft}$')
    axarr[0].plot(list1, list3, label='T$_{magnet}$')
    axarr[0].plot(list1, list4, label='T$_{stator\; tooth}$')
    axarr[0].plot(list1, list5, label='T$_{stator\; yoke}$')
    axarr[0].plot(list1, list6, label='T$_{winding}$')
    axarr[0].plot(list1, list7, label='T$_{pins}$')
    axarr[0].plot(list1, list8, label='T$_{casing}$')
    axarr[0].plot(list1, list9, label='T$_{gearbox}$')
    axarr[0].set_xlabel("Time [s]", fontsize=10)
    axarr[0].set_ylabel("Temperature $[^{\circ}C]$", fontsize=10)
    axarr[0].set_xlim(xmin, xmax) 
    axarr[0].set_ylim(ymin1, ymax1+15) 
#    axarr[0].autoscale(tight=True)
    axarr[0].grid(True)
    axarr[0].legend()
#    plt.xlim((0,694))
#    axarr[0].set_title(file)
    
    axarr[1].plot(list1, list10)
    axarr[1].set_xlabel("Time [s]", fontsize=10)
    axarr[1].set_ylabel("Q [W]", fontsize=10)
    axarr[1].set_xlim(xmin,xmax)
    axarr[1].set_ylim(ymin2, ymax2+5) 
#    axarr[1].autoscale(tight=True)
    axarr[1].grid(True)
#    axarr[1, 0].set_title(file)
    
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.suptitle(file)
    plt.savefig(file + "_complete.png", format='png')
    plt.show()

def main():

# call simulations for all cases 
    simulation(paths1, models1, times, A_i, t_i, htc_i, dir_modelon, dir_lcl, dir_save)
    simulation(paths2, models2, times, A_m, t_m, htc_m, dir_modelon, dir_lcl, dir_save)

# change current directory to results directory
    os.chdir(dir_save)

# plotting functions    
    for file in files_list1:
        dy_mat_func_inverter(file)
    
    for file in files_list2:
        dy_mat_func_motor(file)
        
        
if __name__ == "__main__":
    main()