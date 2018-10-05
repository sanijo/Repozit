# -*- coding: utf-8 -*-
"""
Data analysis script

"""
import pandas as pd
import numpy as np
import time

start_time = time.clock()

log_file_list=['H10C2_0_412_normal_gear_raw']

def data_analysis(log):
    
    log_file=log + ".csv"
    
    print("Analysing " + log_file + "\n")
    
    df = pd.read_csv(log_file, sep=',')

    time1=df['Time']
    time2=df['Time']
    time3=df['Time']
    time4=df['Time']
    value1=df['Qml']
    value2=df['Qmr']
    value3=df['Qil']
    value4=df['Qir']

    #print(value1)
    i=0
    j=[0]
    k=[0]
    l=[0]
    m=[0]
    n=[0]

    while i < (time1.size):
        j.append(time1[i])
        k.append(value1[i])
        l.append(value2[i])
        m.append(value3[i])
        n.append(value4[i])
        i += 1
        
    heat1=pd.DataFrame(
        {'HeatFlow': k,
         'Time': j
        })
    
    time1=heat1['Time']
    value1=heat1['HeatFlow']
        
    HE1=pd.concat([time1, value1], axis=1)
    
    HE1.to_csv("QmotorL_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    
    heat2=pd.DataFrame(
        {'HeatFlow': l,
         'Time': j
        })
    
    time2=heat2['Time']
    value2=heat2['HeatFlow']
    
    HE2=pd.concat([time2, value2], axis=1)
    
    HE2.to_csv("QmotorR_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)

    heat3=pd.DataFrame(
        {'HeatFlow': m,
         'Time': j
        })
    
    time3=heat3['Time']
    value3=heat3['HeatFlow']
        
    HE3=pd.concat([time3, value3], axis=1)
    
    HE3.to_csv("QinverterL_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    
    heat4=pd.DataFrame(
        {'HeatFlow': n,
         'Time': j
        })
    
    time4=heat4['Time']
    value4=heat4['HeatFlow']
    
    HE4=pd.concat([time4, value4], axis=1)
    
    HE4.to_csv("QinverterR_"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)    
    
    print("--- %s seconds spent for analysing %s ---" % (time.clock() - start_time, log_file))


for log in log_file_list:
    data_analysis(log)


print("--- %s seconds spent overall---" % (time.clock() - start_time))   