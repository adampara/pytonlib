#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:18:18 2018

@author: para
"""
from __future__ import print_function

from builtins import str
from builtins import range
from plot_histogram import plot_histogram

def fit_root_polynomial(hist,order,debug=False):
    """
    Locate the peak in a histogram, fit gaussian in a neighborhood, return fit parameters
    """
    

    function = 'pol' + str(order)
    if debug:
        options = 'SQ'
    else:
        options = 'SQ0'
        
    fit_res = hist.Fit(function,options,'')
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            print('fit_root_polynomial: Fit results :')
            for io in range(order+1):
                print(io, fit_res.Parameter(io))
            plot_histogram(hist)
        else:
            print('Fit failed ')
            plot_histogram(hist)


    if stat == 0 :
        par = []
        for iord in range(order+1):
            par.append(fit_res.Parameter(iord))

    else:
        par = []

    return stat,par