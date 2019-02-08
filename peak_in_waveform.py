#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:40 2018

@author: para
"""
from ROOT import TH1F
from fit_gaussian_peak import fit_gaussian_peak

def peak_in_waveform(wf,l_lim = -100, u_lim=100, nb=400, h_wid = 3,debug=False):
    """
    histogram values of te waveform betwee l_lim and u_lim
     fit a gaussian peak around the maximum, +- h_wid
     """

    title = 'peak_in_waveform'
    hist = TH1F(title,title,nb,l_lim,u_lim)

    for val in wf:
        hist.Fill(val)
    
    stat,p1,p2,p3 = fit_gaussian_peak(hist, h_wid, debug=debug)
        
    return   stat,p2   
    