#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:37:25 2022
plot an integrand of a histogram
@author: para
"""
from integrate_array        import integrate_array
from unpack_histogram       import unpack_histogram
from plot_histogram         import plot_histogram

def plot_integrated_histogram(hist):
    """
    show spe charge as a function of the integration window
    """
    
    wfi = hist.Clone()

    nbin,delta,xc,cont,entries = unpack_histogram(wfi)   
    cont_i = integrate_array(cont)
    for i in range(len(cont)):
        wfi.SetBinContent(i+1,cont_i[i])
    plot_histogram(wfi,option='hist')  
    