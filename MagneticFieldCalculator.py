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

def B_flat_coil(I=1,R=0.5e-3,N=1,z=100e-6):
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
    Bc=k*mu0*I*N/(2*R)
    Bz=k*mu0*0.5*R**2*I/pow(z**2+R**2,1.5)
    return Bc,Bz

def B_spiral_coil(NL=2,I=1,d=0.1e-3,width=0.1e-3,rend=0.5e-3,z=100e-6,tlayer=0e-6):
    '''
    Parameters
    ----------
    I : distance between width, current (A)
    L : float, length (m)
    N : Number of turns, optional
    Returns
    -------
     magnetic field
    '''
    n=rend//(d+width)
    Btotalz=0
    Btotalc=0
    for k in range(int(n)):
        Bc,Bz=B_flat_coil(I,(k+1)*(d+width/2),1,z+k*tlayer)
        Btotalc +=NL*Bc
        Btotalz +=NL*Bz
    return Btotalz*1e3,Btotalc*1e3,n
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