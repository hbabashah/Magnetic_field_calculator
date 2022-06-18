# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:54:48 2022

@author: babashah
"""

import numpy as np
mu0=4*np.pi*1e-7
def B_wire(I=1,r=np.array([1])):
    '''
    Parameters
    ----------
    I : integer, current (amper)
    r : integer, radius (meter)

    Returns
    -------
        magnetic field. (T)

    '''
    r=np.array(r)
    return mu0*I/(r*2*np.pi)

def B_solenoid_center(I=1,L=1,N=100):
    '''
    Parameters
    ----------
    I : float, current (A)
    L : float, length (m)
    N : Number of turns, optional
    Returns
    -------
     magnetic field
    '''
    

    # I is amp
    # r is radius m
    k=1 #relative permeability of the core
    return k*mu0*I*N/L

def B_flat_coil(I=1,R=1,N=100):
    '''
    Parameters
    ----------
    I : float, current (A)
    L : float, length (m)
    N : Number of turns, optional
    Returns
    -------
     magnetic field
    '''
    
    # I is amp
    # r is radius m
    k=1 #relative permeability of the core
    return k*mu0*I*N/(2*R)
def L_coil(N=10,R=1,L=1):
    '''
    Parameters
    ----------
    N : number of turns
    A : Coil area (m^2)
    L : Coil Length (m)

    Returns
    -------
    None.
    
    '''
    A=np.pi*R**2
    return mu0*N**2*A/L        
if __name__ == "__main__":
    import pylab as pl
    r=np.linspace(.01,0.09,100)
    pl.plot(r*1e3,1e3*B_wire(1,r))
    pl.xlabel('mm')
    pl.ylabel('mT')
    print(1e3*B_solenoid_center(1,1,100))