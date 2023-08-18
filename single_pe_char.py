#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:58:46 2018

@author: para
"""
from __future__ import print_function
import numpy as np
from weighted_avg_and_std import weighted_avg_and_std

def single_pe_char(wave,ind_peaks,h_width,neigh,debug=False):
    """
    calculate characteristics of single pe peaks in waveform wave
    peak positions are in array ind_peaks, peak has half-width h_with, background is evaluated in 'neigh' bins outside h_width
    """

    name = 'single_pe_char'

    if debug: print(name)
    time = np.linspace(-h_width, h_width, num=2*h_width+1) 
    if debug:  print('time ',time)
 
    charge = []
    t_stamp = []
    t_width = []
    
    for ind in ind_peaks:
        
        bck_l = 0.
        if ind - h_width - neigh > 0:
            bck_l = np.mean(wave[ind - h_width - neigh:ind - h_width])
            
        bck_r = 0.
        if ind + h_width + neigh < len(wave):
            bck_r = np.mean(wave[ind + h_width :ind + h_width + neigh])
            
        bck = 0.5*(bck_l + bck_r)
        
        q = np.sum(wave[ind-h_width:ind+h_width+1] - bck)

        if debug:  
            print(name, time)
            print(name, ' pulse  ',     wave[ind-h_width:ind+h_width+1] - bck)  
        
        #  if pulse is too close to the edge approximate its time and width or if the sum of waveform too close to 0
        min_sum = 1.
        if ind < neigh + h_width or ind > len(wave) - neigh - h_width or np.sum(wave[ind-h_width:ind+h_width+1] - bck) < min_sum:
            av = 0   #  vaue of 'ind' will be added to make the time stamp coincident with the pulse position 
            std = 0
        else:
            av,std = weighted_avg_and_std(time,wave[ind-h_width:ind+h_width+1] - bck)

        charge.append(q)
        t_stamp.append(ind+av)
        t_width.append(std)
        
    return np.asarray(charge),np.asarray(t_stamp),np.asarray(t_width)