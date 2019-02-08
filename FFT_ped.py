#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:27:22 2018

@author: para
"""

import numpy as np

def FFT_ped(wave):
    """
    FFT determination of pedestal 
    """
    

    Y = np.fft.fft(wave)    # fft computing and normalization
    ped = Y[0].real/len(wave)

    return ped
