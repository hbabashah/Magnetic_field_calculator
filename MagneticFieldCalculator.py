# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:54:48 2022

@author: babashah
"""

import numpy as np
def B_wire(I=1,r=np.array([1])):
    r=np.array(r)
    mu0=4*np.pi*1e-7
    # I is amp
    # r is radius m
    return mu0*I/(r*2*np.pi)

def B_solenoid_center(I=1,L=1,N=100):
    mu0=4*np.pi*1e-7
    # I is amp
    # r is radius m
    k=1 #relative permeability of the core
    return k*mu0*I*N/L


if __name__ == "__main__":
    import pylab as pl
    r=np.linspace(.01,0.09,100)
    pl.plot(r*1e3,1e3*B_wire(1,r))
    pl.xlabel('mm')
    pl.ylabel('mT')
    print(1e3*B_solenoid_center(1,1,100))