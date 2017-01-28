# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:52:21 2017

@author: para
"""

import scipy
import numpy as np


def baseline_subtract(wave, low, high):
    """
        for a given waveform wave, use the region low to high to determine
        the baseline, return the waveform with baseline subtracted
    """
    baseline = scipy.mean(wave[low:high])
    wave_sub = wave - baseline

    return wave_sub
