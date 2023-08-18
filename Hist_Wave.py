#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:24:49 2021

@author: para
"""
from builtins import range
def Hist_Wave(hist, wave):
    """
    Fill histograms with a waveform

    """
    for i in range(len(wave)):
        hist.Fill(float(i), wave[i])
