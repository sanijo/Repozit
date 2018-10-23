# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 08:22:20 2018

@author: sanijo.durasevic
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import vectorize

# Define the variables
Q = np.linspace(0.00001667, 0.0001, num=50, endpoint=True) # Flow rate m^3/s (1-6 l/min)
d = np.linspace(0.02, 0.03, num=50, endpoint=True)  # Pipe's diameter m (or hydraulic diametar)
mu = 0.001                 # Water viscosity Pa s @25 C
rho = 1000                 # Water density kg/m^3
L = 1                      # Pipe's length m
e = 0.000007                 # Pipe's rugosity (material dependent) --enter in m-- plastic here

relative_roughnes = lambda e, d: e/d

# This function calculates the velocity of the fluid [m/s]
def vel(Q, d):
    v = 4*Q/(np.pi * d**2)
    return v

    
# This function calculates the friction coefficient Lambda
def lbd(v, d, mu=mu, rho=rho,e=e):
    reynolds = rho*v*d/mu
    print("Reynolds number: " + str(reynolds))
    # If RE < 2320 flow is laminar, otherwise it is turbulent
    if reynolds <= 2320:
        lbda = 64/reynolds
    else:
        if relative_roughnes(e, d) > 0.000001:
        # Swamee–Jain equation (Re = 5000-10^8, e/d=0.000001-0.5)
            #lbda = 0.25/(np.log10(e/(3.7*d)+5.74/(reynolds**0.9)))**2
            lbda = 0.11*(e/d+68/reynolds)**0.25
        else:
        #Aldsul equation
            lbda = 0.11*(e/d+68/reynolds)**0.25
    return lbda

# This function calculates the pressure drop [Pa]
def pressureDrop(Q, d, L=L):
    v = vel(Q, d)
    pDrop = (lbdv(v,d)) * (L / d) * (0.5 * rho * v**2)
    return pDrop

# Function to plot the contour plot
def contour(X, Y, Z, N=20):
    plt.figure()
    CS = plt.contour(X, Y, Z, N)
    plt.clabel(CS, inline=1, fontsize=8)
    plt.title('Pressure drop(Pa)')
    plt.xlabel('Q (m$^3$/h)')
    plt.ylabel('d (mm)')
    plt.show()

# Function to make a 3d plot
def dplot(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(Q, d, pdrop, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.set_xlabel('Q (m$^3$/h)')
    ax.set_ylabel('d (mm)')
    ax.set_zlabel('$\Delta p$ (Pa)')
    ax.set_title('Pressure drop (Pa)')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

# Vectorize function for calculating lambda
lbdv = vectorize(lbd)

# Grid
Q, d = np.meshgrid(Q, d)

# Calculate pressure drop [Pa]
pdrop = pressureDrop(Q, d)

# Convert pressure drop in meters
pdrop = pdrop  / (9.81 * rho)

# Convert pressure drop in bar
#pdrop = pressureDrop(Q, d) / (10**5)

# Convert Q in m^3/h and d in mm (for better visualization)
Q = Q * 3600 
d = d * 1000

# Plot
dplot(Q,d,pdrop)

# Contour plot
contour(Q,d,pdrop)