#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:52:51 2018

@author: para
"""

def combine_waveforms(wave,ind,cont,thresh = -999):
    """
    add waveformr cont aith indices ind to the waveform wave
    """
    
    for i in ind:
        if cont[i] > thresh:
            wave[i] += cont[i]