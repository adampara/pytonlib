#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 22:08:01 2018

@author: para
"""

import numpy as np
from integrate_array import integrate_array
from fitpol import fitpol

def improve_pedestal(wave, debug=False):
    
    """
    fit slope to the intergrated raw waveform
    """
    
    int_wave = integrate_array(wave) 
    x_arr = np.linspace(0,len(int_wave)-1,len(int_wave))

    fitr,fitf,cov = fitpol(x_arr, int_wave, 1, [], maxcut = 52000, plot=debug, debug=debug)
    
    return fitr[0]

