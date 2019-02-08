#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:18:18 2018

@author: para
"""

from plot_histogram import plot_histogram

def fit_gaussian_peak(hist,half_width=5,debug=False):
    """
    Locate the peak in a histogram, fit gaussian in a neighborhood, return fit parameters
    """
    
    max_pos = hist.GetBinCenter(hist.GetMaximumBin())

    fit_res = hist.Fit('gaus','SQ0','', max_pos-half_width, max_pos+half_width)
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            print 'fit_gaussian peak: Fit results :', fit_res.Parameter(0), fit_res.Parameter(1), fit_res.Parameter(2)
            plot_histogram(hist)
        else:
            print 'Fit failed '
        plot_histogram(hist)


    if stat == 0 :
     
        p1 = fit_res.Parameter(0)
        p2 = fit_res.Parameter(1)
        p3 = fit_res.Parameter(2) 
    else:
        p1 = 0
        p2 = 0
        p3 = 0

    return stat,p1,p2,p3