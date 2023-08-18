#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:18:18 2018

@author: para
"""
from __future__ import print_function

from plot_histogram import plot_histogram

def fit_gaussian_peak(hist,half_width=5,debug=False, fit_opt='SQ0',peak_pos=-9999):
    """
    Locate the peak in a histogram (if peak_pos=-9999), fit gaussian in a neighborhood, return fit parameters
    """

    if debug:
        print ('   fit histogram', hist.GetTitle())
        
    if peak_pos == -9999:  
        max_pos = hist.GetBinCenter(hist.GetMaximumBin())
    else:
        max_pos = peak_pos

    fit_res = hist.Fit('gaus',fit_opt,'', max_pos-half_width, max_pos+half_width)
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            print('fit_gaussian peak: Fit results :', fit_res.Parameter(0), fit_res.Parameter(1), fit_res.Parameter(2))
            print('Maximum position ', max_pos, ' Fit range ', max_pos-half_width, max_pos+half_width)
            plot_histogram(hist)
        else:
            print('Fit failed ')
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

def fit_gaussian_peak_full(hist,half_width=5,debug=False, fit_opt='SQ0',peak_pos=-9999):
    """
    Locate the peak in a histogram (if peak_pos=-9999), fit gaussian in a neighborhood, return fit parameters
    return the complete fit_res structure
    """
    if debug:
        print ('   fit histogram', hist.GetTitle())
        
    if peak_pos == -9999:  
        max_pos = hist.GetBinCenter(hist.GetMaximumBin())
    else:
        max_pos = peak_pos

    fit_res = hist.Fit('gaus',fit_opt,'', max_pos-half_width, max_pos+half_width)
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            
            print('fit_gaussian peak: Fit results :', fit_res.Parameter(0), fit_res.Parameter(1), fit_res.Parameter(2))
            print('Maximum position ', max_pos, ' Fit range ', max_pos-half_width, max_pos+half_width)
            plot_histogram(hist)
        else:
            print('Fit failed ')
            plot_histogram(hist)


    if stat == 0 :
     
        p1 = fit_res.Parameter(0)
        p2 = fit_res.Parameter(1)
        p3 = fit_res.Parameter(2) 
    else:
        p1 = 0
        p2 = 0
        p3 = 0

    return fit_res

from ROOT           import TF1

def fit_gaussian_peak_limits(hist, val_min, val_max, half_width=5,debug=False, fit_opt='SQ0',peak_pos=-9999):
    """
    Locate the peak in a histogram (if peak_pos=-9999), fit gaussian in a neighborhood, return fit parameters
    """

    if debug:
        print ('   fit histogram', hist.GetTitle(), '  fit options  ', fit_opt)
        
    if peak_pos == -9999:  
        max_pos = hist.GetBinCenter(hist.GetMaximumBin())
    else:
        max_pos = peak_pos

    #     fit constraints  
    f1 = TF1("f1", "gaus", max_pos-half_width, max_pos+half_width)

    f1.SetParameter(0, hist.GetBinContent(hist.GetXaxis().FindBin(max_pos)))
    f1.SetParameter(1, max_pos)
    f1.SetParameter(2, half_width/10.)
    
    f1.SetParLimits(0, 0. , 9.e6)
    f1.SetParLimits(1, val_min, val_max)
    f1.SetParLimits(2, 0., half_width)
    
    print ('  lower limit ', val_min,'  upper limit ', val_max, '   half_width  ', half_width)
    
    fit_res = hist.Fit(f1,fit_opt+'B','', max_pos-half_width, max_pos+half_width)
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            print('fit_gaussian peak: Fit results :', fit_res.Parameter(0), fit_res.Parameter(1), fit_res.Parameter(2))
            print('Maximum position ', max_pos, ' Fit range ', max_pos-half_width, max_pos+half_width)
            plot_histogram(hist)
        else:
            print('Fit failed ')
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