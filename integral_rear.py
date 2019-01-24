# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:52:17 2019

@author: sanijo.durasevic
"""

import platform
import matplotlib
#matplotlib.use('Qt5Agg')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
from scipy.interpolate import RectBivariateSpline
import os
import sys
from datetime import date
import time

start_time = time.clock()

today = str(date.today().isoformat())
dir_save = os.getcwd() + '\\' + today + '_input_data_REAR'
os.makedirs(dir_save, exist_ok=True)

log_file_list=['C02_Grobnik_20181112', 'C02_Nardo_Oval2_20181112']

# Load losses data
lossData = np.loadtxt('Eff_rear.csv', delimiter=',')
torques = lossData[0,1:]
powers = lossData[1:,0]
losses = lossData[1:,1:]

# Make loss calculators
motorLoss = RectBivariateSpline(powers, torques, losses)
# Call this function like this: Q = motorLoss(power, torque, grid=False)

#for 0 Nm torque generated heat is 100 W
#inverterLoss = lambda t: 100 + 24.1463*np.absolute(t)

def rear(log):
    
    log_file=log+".csv"
    
    print(log_file)
    
    # Your log file is dirty. Load it so that it is clean
    df = pd.read_csv(log_file, sep=',', skiprows=[1])
    df.drop_duplicates(keep='last', inplace=True)
    # Also cut it down to a manageable size
    df = df[::10]   
    
    # Time conversion
    df['Time'] = round(df['Time'], 2)
    
    # Calculate inverter heat [W] -> eta = 90 %
    df['InverterHeatRL'] = round(abs(1000*df['PT.Motor2.PwrElec']*0.1), 2)
    df['InverterHeatRR'] = round(abs(1000*df['PT.Motor3.PwrElec']*0.1), 2)
#    df['InverterHeatRL'] = round(inverterLoss(df['PT.Motor2.Trq']), 2)
#    df['InverterHeatRR'] = round(inverterLoss(df['PT.Motor3.Trq']), 2)
    
    # Load motor power data [conversion kW -> W]   
    df['PT.Motor2.PwrElec']=1000*df['PT.Motor2.PwrElec']
    df['PT.Motor3.PwrElec']=1000*df['PT.Motor3.PwrElec']

############################################################################### 
    """calculating average inverter efficiency"""
    
    df['eta_inv']=100*(df['InverterHeatRL']/abs(df['PT.Motor2.PwrElec']))
    df2 = pd.DataFrame(df.iloc[4:,21])
    print(100-df2.mean())
###############################################################################
    
    # Load motor speed data [conversion rad/s -> rpm]
    df['PT.Motor2.rotv']=9.55*df['PT.Motor2.rotv']    
    df['PT.Motor3.rotv']=9.55*df['PT.Motor3.rotv']
    
    # Load speed data
    df['Speed'] = round(df['Car.v'], 2)
    
    # Calculate motor heat loss
    df['MotorHeatRL'] = round(abs(df['PT.Motor2.PwrElec']*(1-motorLoss( df['PT.Motor2.PwrElec'],df['PT.Motor2.rotv'], grid=False))), 2)
    df['MotorHeatRR'] = round(abs(df['PT.Motor3.PwrElec']*(1-motorLoss( df['PT.Motor3.PwrElec'],df['PT.Motor3.rotv'], grid=False))), 2)
    
    #Save data to .csv  
    os.chdir(dir_save)      
    columnsToSave = ['Time','MotorHeatRL', 'MotorHeatRR', 'InverterHeatRL', 'InverterHeatRR']
    df[columnsToSave].to_csv("HEAT_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    columnsToSave = ['Time','Speed']
    df[columnsToSave].to_csv("SPEED_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    os.chdir("..")
      
def main():
      
    for log in log_file_list:
        rear(log)
        
    print("--- %s seconds ---" % (time.clock() - start_time)) 
        
if __name__ == "__main__":
    main()
