#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:59:49 2018

@author: para
"""
import numpy as np
from ac_coupl import ac_coupl
from peak_in_waveform import peak_in_waveform

def saturation_corr(wave,max_pos,pulse_end,satur_corr,tau):
    """
    correct raw waveform by adding 'satur_corr' at the time bin 'max_pos'
    make deconvolution and caalculate baseline shift
    """

    n_wave = np.copy(wave)
    n_wave[max_pos] = n_wave[max_pos] + satur_corr

    wf_corr,bs =  ac_coupl(n_wave,tau)
    stat,bl_shift = peak_in_waveform(wf_corr[pulse_end:pulse_end+1000],debug=False)
    
    return stat,bl_shift,wf_corr
