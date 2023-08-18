#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:27:45 2022

@author: para
"""

from integrate_array       import integrate_array
from unpack_histogram      import unpack_histogram

def integrate_histogram(hist):
    """
    integrate the histogram    

    """
    hist_i = hist.Clone()
    hist_i.SetTitle(hist.GetTitle() + ' , integral')
    
    nbin,delta,xc,cont,entries = unpack_histogram(hist)   
    cont_i = integrate_array(cont)
    for i in range(len(cont)):
        hist_i.SetBinContent(i+1,cont_i[i])

    return hist_i    