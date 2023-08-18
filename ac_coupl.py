#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:03:48 2018

@author: para
"""
from builtins import range
from math import exp
import numpy as np


def ac_coupl(wf,tau,bss=0):
    
    """
    correct the RC-coupled raw waveform using RC constant tau
    return corrected waveform and the baseline shift
    modified Thu Feb  3 16:47:33 CST 2022: 
        add the initial baseline shift  bss as an optional free parameter 
    """
    att = exp(-tau)
    
#    bs = [0 for i in range(len(wf))]
#    wf_corr = [0 for i in range(len(wf))]
    bs = np.zeros(len(wf))
    wf_corr = np.zeros(len(wf))


    for i in range(1,len(wf)):

        wf_corr[i] = wf[i]-bss*att
        bss = bss*att - wf_corr[i]*tau
        
        bs[i] = bss

    return np.asarray(wf_corr),bs

