#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:32:44 2018

@author: para
"""

import numpy as np 
from FFT_ped import FFT_ped
from smooth_wave import smooth_wave
import matplotlib.pyplot as plt

def find_pulses(wavef, cut=50, cut_low = 5, nlow = 5,nsm_sipm = 5,  debug=False):
    """ 
    find all regions where waveform is above cut
    smooth_out the waveform, subtract pedestal
    
    """

    name = '  ---->  find pulses : '        

    smooth_SiPM = smooth_wave(wavef ,nsm_sipm)
    ped_sipm = FFT_ped(smooth_SiPM)
    waveform = smooth_SiPM-ped_sipm

    beg = []
    end = []
     
    low  = True
    high = False
    n_below = 0
    
    for ind in range(len(waveform)):

        val = waveform[ind]
        
        if val > cut:  
            if high: 
                continue
            else:
                high = True
                low  = False
                n_below = 0
                beg.append(ind)
        else:
            if low:
                continue
            else:
                #   to terminate the pulse we require nlow consecutive samples belo cut_low
                if val > cut_low : continue
                n_below +=1
                if n_below > nlow:
                    end.append(ind-1)
                    low  = True
                    high = False
    
    if high:
        end.append(ind-1)

    if debug:
        print name, 'pulses found above threshold of ', cut
        for b,e in zip(beg,end):
            print  'From ', b, ' to ',e

        plt.figure()
        plt.plot(waveform)
        plt.title('  find_pulses: smooth SiPM waveform after pedestal')
        plt.show()
        
    return np.asarray(beg),np.asarray(end)
    
