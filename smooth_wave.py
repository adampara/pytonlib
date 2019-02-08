# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:47:48 2017

@author: para
"""

import numpy as np


def smooth_wave(wf, nsmooth):
    """
    smooth out the waveform by averaging with nsmooth samples before and after

    """
    lenwf = len(wf)
    nwfm = np.zeros(lenwf)
    
    for i in range(lenwf):

        nl = max(0,i-nsmooth)
        nu = min(lenwf-1,i+nsmooth)

        nwfm[i] = sum(wf[nl:nu])/(nu-nl)   
        
    return nwfm

def smooth_wave_nzero(wf, nsmooth):
    """
    smooth out the waveform by averaging with nsmooth samples before and after
    ignore zero values for everaging

    """
    lenwf = len(wf)
    nwfm = np.zeros(lenwf)
    
    for i in range(lenwf):

        nl = max(0,i-nsmooth)
        nu = min(lenwf-1,i+nsmooth)

        sumval  = sum(wf[nl:nu])
        
        nz = np.count_nonzero(wf[nl:nu])   
        if nz > 0:
            nwfm[i] = sumval/nz
        else:
            nwfm[i] = 0
            
    return nwfm
