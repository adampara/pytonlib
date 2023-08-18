#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:29:30 2018

@author: para
"""
"""
combine short pulses
"""


            #   short pulses structure  pe_set = (ind_peaks_pre,charge_pre,tstamp_pre,twidth_pre)
            #find_short_pulses(wf_corr_fin, pmt, event, pe_front, pe_back, ntrigger, pulse_end, nsmooth=5 ,debug=False)
from builtins import zip
def combine_short_pulses(short_p,count,pe_set):


    ind = pe_set[0]     #  position the pulse at the leading edge
    ch  = pe_set[1]

    for ts, sig in zip(ind,ch):

        short_p[int(ts)] += sig
        count[int(ts)] += 1