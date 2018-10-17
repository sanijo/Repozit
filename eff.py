import platform
import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
from scipy.interpolate import RectBivariateSpline

start_time = time.clock()

log_file_list=['C2_0_100_0_10x_wo_reg_raw',
               'C2_0_200_0_6x_wo_reg_raw',
               'C2_0_330_hold_raw',
               'C2_0_412_normal_gear_raw',
               'C2_Grobnik_100_0_SoC_wo_reg_raw',
               'C2_Nardo_Handling_100_0_SoC_wo_reg_raw',
               'C2_Nardo_Oval_1_raw',
               'C2_Nardo_Oval_2_wo_reg_raw',
               'C2_Nurburgring_100_0_SoC_wo_reg_raw']

#log_file_list=['C2_0_100_0_10x_wo_reg_raw']

# Load losses data
lossData = np.loadtxt('motorLosses.csv', delimiter=';')
torques = lossData[0,1:]
print(torques)
speeds = lossData[1:,0]
print(speeds)
losses = lossData[1:,1:]
print(losses)

# Make loss calculators

motorLoss = RectBivariateSpline(speeds, torques, losses)
# Call this function like this: Q = motorLoss(speed, torque, grid=False)
#inverterLoss = lambda w,t: 100 + 24.1463*np.absolute(w)
#NOVO
inverterLoss = lambda t: 100 + 24.1463*np.absolute(t)


def data_analysis(log):
    
    log_file=log + ".csv"
    
    print("\nAnalysing " + log_file + "\n")
    start_time_for_file = time.clock()
    
    # df = pd.read_csv(log_file, sep=',')
    # Your log file is dirty. Load it so that it is clean
    df = pd.read_csv(log_file, sep=',', skiprows=[1,2])
    # Also cut it down to a manageable size
#    df = df[::100]
    
    # Now instead of doing that, use the new heat generation functions
    df['Speed'] = df['Car.v']
        
    #NOVO
    df['MotorHeatRL'] = motorLoss(df['PT.Motor2.rotv'], df['PT.Motor2.Trq'], grid=False)
    df['MotorHeatRR'] = motorLoss(df['PT.Motor3.rotv'], df['PT.Motor3.Trq'], grid=False)    
    df['InverterHeatRL'] = inverterLoss(df['PT.Motor2.Trq'])
    df['InverterHeatRR'] = inverterLoss(df['PT.Motor3.Trq'])
   
        
    columnsToSave = ['Time','MotorHeatRL', 'MotorHeatRR', 'InverterHeatRL', 'InverterHeatRR']
    df[columnsToSave].to_csv("H10"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    columnsToSave = ['Time','Speed']
    df[columnsToSave].to_csv("S10"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)

#conversion from W to kW  
    df['MotorHeatRL']=0.001*df['MotorHeatRL']
    df['MotorHeatRR']=0.001*df['MotorHeatRR']
    df['InverterHeatRL']=0.001*df['InverterHeatRL']
    df['InverterHeatRR']=0.001*df['InverterHeatRR']
    
    time1 = df['Time']
    motorPwr = df['PT.Motor2.PwrElec']
    #print(motorPwr[300:400])
    motorHeat=df['MotorHeatRL']
    
    fig, ax = plt.subplots()
    motorPwr.plot(x='Time', y=['PT.Motor2.PwrElec'])
    plt.xlabel("Time [s]")
    plt.ylabel("Power [kW]")
    plt.show()
    
    list1 = []
    list2 = []
    i = 0
    j = 0
   # print(time1)
#    print(time1.size)

        
    while j < (time1.size-1):
        list1.append(time1[i])
        #print(motorHeat[i]/motorPwr[i])
        if motorPwr[i] <= 20: # motorHeat/motorPower is to small for lower values
            pom=0
            list2.append(pom)
        else:
            list2.append(100-(100*motorHeat[i]/motorPwr[i]))
        i+=1
        j+=1
        #print(list2)
   # print(list1)
  #  print(list2)

#Create new dataframe
    effikasnost=pd.DataFrame(
        {'Eff': list2,
         'Time': list1
        })

    effikasnost.plot(x='Time', y='Eff')
    plt.xlabel("Time [s]")
    plt.ylabel("eff [%]")
#   plt.axis([0, 200, 0, 10])
    plt.show()
    
    #df.plot(x='Time', y=['PT.Motor2.PwrElec','MotorHeatRL','InverterHeatRL','PT.Motor2.Trq'])
    df.plot(x='Time', y=['PT.Motor2.PwrElec','MotorHeatRL'])
    plt.xlabel("Time [s]")
    plt.ylabel("Power [kW]")
    plt.show()
    
    print("\n--- %s seconds spent for analysing %s ---" % (time.clock()-start_time_for_file, log_file))
    
for log in log_file_list:
    data_analysis(log)


print("\n--- %s seconds spent overall ---" % (time.clock() - start_time)) 