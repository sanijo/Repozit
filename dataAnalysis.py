# -*- coding: utf-8 -*-
"""
Data analysis script

"""
import pandas as pd
import numpy as np
import time

start_time = time.clock()

log_file_list=['HeatFlow']

def data_analysis(log):
    
    log_file=log + ".csv"
    
    print("Analysing " + log_file + "\n")
    
    df = pd.read_csv(log_file, sep=',')

    time1=df['Time']
    value1=df['Q_flow']

    #print(value1)
    i=0
    j=[]
    k=[]

    while i < (time1.size-1):
        j.append(time1[i])
        k.append(value1[i])
        i += 20
 
    heat=pd.DataFrame(
        {'HeatFlow': k,
         'Time': j
        })

    time1=heat['Time']
    value1=heat['HeatFlow']

    HE=pd.concat([time1, value1], axis=1)
    
    HE.to_csv("analised"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
    
    print("--- %s seconds spent for analysing %s ---" % (time.clock() - start_time, log_file))


for log in log_file_list:
    data_analysis(log)


print("--- %s seconds spent overall---" % (time.clock() - start_time))   