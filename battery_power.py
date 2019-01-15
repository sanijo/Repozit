# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:50:09 2018

@author: sanijo.durasevic
"""

import platform
import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
from scipy.interpolate import RectBivariateSpline
import os
import sys

start_time = time.clock()

today = str(date.today().isoformat())
dir_save = os.getcwd() + '\\' + today + '_1D_input_data'
os.makedirs(dir_save, exist_ok=True)

log_file_list=['C02_WLTC_20181112', 'C02_Grobnik_20181112']


def pw(log):
    
    log_file=log + ".csv"
    
    print("\nAnalysing " + log_file + "\n")
    
    df = pd.read_csv(log_file, sep=',', skiprows=[1,2])
    df.drop_duplicates(keep='last', inplace=True)
    
    time = df['Time']
    value = 1000*df['PT.PwrSupply.HV1.Pwr'] #converted from kW to W
        
    i = 0
    j = [0]
    k = [0]
    
    while i < (time.size):
        j.append(round(time[i],2))
        k.append(round(value[i], 2))
        i += 10
        
    power = pd.DataFrame({'Time' : j, 'BatteryPower' : k})  
    
    os.chdir(dir_save)       
    columnsToSave = ['Time','BatteryPower']
    power[columnsToSave].to_csv("POWER_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    os.chdir('..')
    
def speed(log):
    
    log_file=log + ".csv"
    
    print("\nAnalysing " + log_file + "\n")
    
    df = pd.read_csv(log_file, sep=',', skiprows=[1,2])
    df.drop_duplicates(keep='last', inplace=True)
    
    time = df['Time']
    value = df['Car.v'] #km/h
        
    i = 0
    j = [0]
    k = [0]
    
    while i < (time.size):
        j.append(round(time[i],2))
        k.append(round(value[i], 2))
        i += 10
        
    speed = pd.DataFrame({'Time' : j, 'Speed' : k})  

    os.chdir(dir_save)       
    columnsToSave = ['Time','Speed']
    speed[columnsToSave].to_csv("SPEED_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    os.chdir('..')

def main():
    
    for log in log_file_list:
        pw(log)

    for log in log_file_list:
        speed(log)

    print("\n--- %s seconds spent overall ---" % (time.clock() - start_time)) 

if __name__ == "__main__":
    main()
