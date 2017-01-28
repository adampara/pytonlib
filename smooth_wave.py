# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:47:48 2017

@author: para
"""
import scipy
import numpy as np


def smooth_wave(wf, nsmooth):
    """
    smooth out the waveform by averaging with nsmooth samples before and after

    """
    nwfm = []
    for i in range(len(wf)):
        if i > nsmooth and i < len(wf)-nsmooth:
            nwfm.append(scipy.mean(wf[i-nsmooth:i+nsmooth]))
        else:
            nwfm.append(wf[i])

    return np.array(nwfm)
