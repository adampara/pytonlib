#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:27:22 2018

@author: para
"""
from __future__ import division

from past.utils import old_div
import numpy as np

def FFT_ped(wave):
    """
    FFT determination of pedestal 
    """
    

    Y = np.fft.fft(wave)    # fft computing and normalization
    ped = old_div(Y[0].real,len(wave))

    return ped
