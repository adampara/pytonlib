#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:06:07 2022
normalize histogram to represent average per event assuming 'mult' 
entries per event are histogrammed (for example waveforms)

@author: para
"""

def normalize_histogram(hist, mult):
    
    n_entries = hist.GetEntries()
    
    n_event = n_entries/mult
    
    hist.Scale(1./n_event)