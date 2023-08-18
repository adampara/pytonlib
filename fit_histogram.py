#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:18:18 2018

@author: para
"""
from __future__ import print_function

from plot_histogram import plot_histogram

def fit_histogram(hist,fun='gaus',debug=False,xlow=-9999,xup=9999999):
    """
    fit histogram with function 'fun'
    """
    
    fit_res = hist.Fit(fun,'SQ0','',xlow,xup)
#    print hist
#    print fun
    stat =     int(fit_res)

    if debug:
        if stat == 0:
            print('fit_histogram: Fit results :', fit_res)
        else:
            print('Fit failed ')
        plot_histogram(hist)


    return stat,fit_res