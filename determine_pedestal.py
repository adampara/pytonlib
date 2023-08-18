#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:43:44 2018

@author: para
"""
from __future__ import print_function

from ROOT import TH1F
import matplotlib.pyplot as plt
import numpy as np
from plot_histogram import plot_histogram

def determine_pedestal(wave, debug=False, title=' '):
    """
    find pedestal from a gaussian fit around the most probable value
    """

    if debug:

        plt.plot(wave)
        plt.title(' determine_pedestal: waveform'+title )
        plt.show()
        print(' sample ',wave[0:10])
        
    occurances = np.bincount(wave)
        
    nw = 200
    values = TH1F('values', 'values of waveforms' + title, nw, np.argmax(occurances)-0.5*nw,np.argmax(occurances)+0.5*nw)
    
    for v in wave:
        values.Fill(v)
        
    max_pos = values.GetBinCenter(values.GetMaximumBin())

    fit_res = values.Fit('gaus','SQ0','',max_pos-5.,max_pos+5)

    if debug:
        print('determine pedestal, pedestal  ', fit_res.Parameter(1))        
        plot_histogram(values)
        
    values.Delete()
    
    return fit_res.Parameter(1)
