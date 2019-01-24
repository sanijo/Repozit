# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:14:03 2019

@author: sanijo.durasevic
"""

import numpy as np
import matplotlib.pyplot as plt

"""solving du/dt +u*du/dx = 0"""

nx = 41
dimension = 2
dx = dimension / (nx-1)
nt = 20
dt = .025
c = 1
Co_max = 1

u = np.ones(nx)
u[int(.5 / dx) : int(1 / dx +1)] = 2
plt.plot(np.linspace(0,2,nx), u)

un = np.ones(nx)

for t in range(nt):
    un = u.copy()
#    plt.plot(np.linspace(0,2,nx))
    
    for i in range (1, nx):
#        Co = un[i]*dt/dx #non-linear convection
        Co = c * dt / dx #linear convection
        u[i] = un[i] - Co * (un[i] - un[i-1])
        print('Co: ' + str(Co))

plt.plot(np.linspace(0,2,nx), u)
print(u)