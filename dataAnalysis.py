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
    
    log_file=log+".csv"
    
    print(log_file)
    
    df = pd.read_csv(log_file, sep=',')

    time1=df['Time']
    value1=df['Q_flow']
    #value2=df['PT.PwrSupply.HV1.Pwr']
#    print(value1)
    i=1
    j=[0]
    k=[0]
    #w=[0]
    while i<(time1.size-1):
        j.append(time1[i])
        k.append(value1[i])
        #n=abs(float(value2[i])*0.07)
        #w.append(n)
        i+=20
    
 
#    if log_file=='C2_Driving_Cycles_C2_6_times_0_200_kmph_regen_on.csv':
#        m=1
#        l=len(j)-1
#        
#        while m<=6:
#            b=len(j)-1
#            x=0
#            while x<=l:
#                c=float(j[x])+float(j[b])
#                j.append(c)
#                k.append(value1[x])
#                w.append(value2[x])
#                x+=1
#            print(j)
#            m+=1
 
    speed=pd.DataFrame(
        {'HeatFlow': k,
         'Time': j
        })
#    heat=pd.DataFrame(
#        {'Heat': w,
#         'Time': j
#        })

    time1=speed['Time']
    value1=speed['HeatFlow']
#    value2=heat['Heat']


    
    HE=pd.concat([time1, value1], axis=1)
#    SP=pd.concat([time1, value1], axis=1)

#    print(value2)
    
    HE.to_csv("analised"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False)
#    SP.to_csv("xS10"+log+".csv", sep='\t', encoding='utf-8', index=False, header=False) 

for log in log_file_list:
    data_analysis(log)


print("--- %s seconds ---" % (time.clock() - start_time))   