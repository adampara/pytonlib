#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:18:27 2018

@author: para
"""

from builtins import range
from detect_peaks import detect_peaks
import numpy as np

def find_peaks_rising(wave, thresh, separation, windl, windr):
    """
    find peaks with rising edge above the preceeding waveform, average of [peak-windl,peak-windr]
    """

    ind_peaks = detect_peaks(wave, mph = thresh, mpd =separation, threshold= 0, show=False) 
    
    del_peak = []        
    for i in range(len(ind_peaks)):
        
        if ind_peaks[i] < windl:
            del_peak.append(i)
        else:

            if wave[ind_peaks[i]]  - np.mean(wave[ind_peaks[i]-windl:ind_peaks[i]-windr]) < thresh:
                del_peak.append(i)
     
    final_peaks = np.delete(ind_peaks,del_peak) 
       
    return final_peaks