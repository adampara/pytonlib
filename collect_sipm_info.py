#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:34:33 2018

@author: para
"""
from __future__ import division

from builtins import zip
from builtins import range
from past.utils import old_div
import numpy as np
from combine_waveforms import combine_waveforms

def collect_sipm_info(sipmwf, iev, nsipm, len_sipm, ped, spe, sipm_x, sipm_y, noisy, cut_e = 0.5):
    
    """
    process raw info from SiPMs
    collect SiPM waveform profile 
    collect x,y,z information in time stamps
    """

    ev_sipm = np.zeros(len_sipm)
#        fig = plt.figure()
#        ax = fig.add_subplot(111, projection='3d')
    

    ts_x = {}   # lists of x positins in a time slice
    ts_y = {}   # lists of y positins in a time slice
    ts_e = {}   # lists of energy deposits in a time slice
    
    for ts in range(0,len_sipm):
        ts_x[ts] = []
        ts_y[ts] = []
        ts_e[ts] = []
        
    for sipm in range(nsipm):
 
        if sipm in noisy :  continue
    
        nzi = np.nonzero(sipmwf[sipm][iev])[0]                 # indices on non-zero elements
        nz = old_div((sipmwf[sipm][iev][nzi] - ped[sipm]),spe[sipm])    # values of non-zero elements (in pe)
        
        xv = np.full(len(nzi),fill_value=sipm_x[sipm])
        yv = np.full(len(nzi),fill_value=sipm_y[sipm])

        for x,y,t,e in zip(xv,yv,nzi,nz):

            if e>cut_e:
                ts_x[t].append(x)
                ts_y[t].append(y)
                ts_e[t].append(e)
      
        combine_waveforms(ev_sipm,nzi,old_div((sipmwf[sipm][iev]-ped[sipm]),spe[sipm]),thresh=0.5) #  collect contribution of each SiPM to the total waveforrm
    
    for t in ts_x:
        ts_x[t] = np.asarray(ts_x[t])
        ts_y[t] = np.asarray(ts_y[t])
        ts_e[t] = np.asarray(ts_e[t]) 
        
    return ev_sipm, ts_x, ts_y, ts_e
