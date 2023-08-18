#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:02:52 2018

@author: para
"""
from __future__ import print_function

from find_peaks_rising import find_peaks_rising
from single_pe_char import single_pe_char
from smooth_wave import smooth_wave
import matplotlib.pyplot as plt

def find_short_pulses(wf_corr_fin, pmt,  pe_front, pe_back, ntrigger, pulse_end, nsmooth=5 ,debug=False):
    
    """
    find short PMT pulses before and after the main pulse
    """
 
    name = '--------> find_short_pulses: '
    
    if debug:
        print(name,'  ntrigger = ',ntrigger,'   pulse_end =', pulse_end)
    #  look for narrow peaks before and after the peak            
    thresh = 1.5
    separation = 5

    npost = pulse_end + 200
          
    windl = 10
    windr = 5
    h_width = 5
    neigh = 5
    safe = 100       #  avoind edges 
    margin = windl+h_width+safe
    
    wf_corr_smooth = smooth_wave(wf_corr_fin,nsmooth)
    
    ind_peaks_pre = find_peaks_rising(wf_corr_smooth[margin:ntrigger], thresh, separation, windl, windr )  + margin
    ind_peaks_post = find_peaks_rising(wf_corr_smooth[npost:-margin], thresh, separation, windl, windr) + npost

    charge_pre,tstamp_pre,twidth_pre = single_pe_char(wf_corr_fin,ind_peaks_pre,h_width,neigh,debug=False)    
    charge_post,tstamp_post,twidth_post = single_pe_char(wf_corr_fin,ind_peaks_post,h_width,neigh,debug=False)
    


    pe_front[pmt] = (ind_peaks_pre,charge_pre,tstamp_pre,twidth_pre)
    pe_back[pmt] = (ind_peaks_post,charge_post,tstamp_post,twidth_post)

    if debug:
        print(name, 'pe_front', ind_peaks_pre)
        print(name, '  pe bac ', ind_peaks_post)
        plt.figure()
        plt.plot(wf_corr_fin)
        plt.plot(wf_corr_smooth)
        plt.title('corrected waveform, single_pe')
        plt.show()
