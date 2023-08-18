#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:49:38 2018

@author: para
"""
from __future__ import print_function
from builtins import zip
from builtins import range
import numpy as np
import matplotlib.pyplot as plt

def fitpol(xr,yr, deg, dyr, plot=False, title='polfit fit', xcut = -9999., 
           maxcut = 999999., debug = False, xint=0,
           x_ax_lab='', y_ax_lab=''):
    """
    Fit polynomial of a degreee deg
    limit the fitted range to be within [xcut,maxcut] range
    return intercept (constant term) at x=xint
    """
    
    if debug:
        print('fit polynomial of ',deg,' degree. Data to be fitted')
        for xf,yf in zip(xr,yr):
            print('     x, y   =  ', xf, yf)
            
    #  remove data below xcut

    #  if no errors are given assign 1. as an error
    if len(dyr) < len(yr):
        dyr = np.ones(len(yr))
        
    x  = []
    y  = []
    dy = []
    
    for xf,yf,dyf in zip(xr,yr,dyr):
        if xf > xcut and xf < maxcut:
            x.append(xf-xint)
            y.append(yf)
            dy.append(dyf)
        else:
            print(' Data discarded, out of requested range, x,y,dy = ', xf, yf, dyf)
        
    #  convert to numpy arrays 
    x = np.asarray(x,dtype=np.float64)
    y = np.asarray(y)
    dy = np.asarray(dy)
    
    if len(x) > deg:

        fitr,cov = np.polyfit(x,y,deg,cov=True)
        
        #     here is a fix for a feature of fitpol
        if len(x) > deg +2:
            pass
        else:
            cov = -cov
            
        if debug:
            
            print('fitpol:   fit results       ', fitr)
            print('          covariance matrix ', cov)
        
        fitf = x*0.0
        for p in range(deg+1):
            fitf = fitf + fitr[p] * x **(deg-p)
        
        if (plot):
            plt.errorbar(x,y,yerr=dy,fmt="*")
            plt.plot(x,fitf)
            plt.title(title)
            plt.xlabel(x_ax_lab)
            plt.ylabel(y_ax_lab)
            plt.grid()
            plt.show()
    else:
        print(' insufficient data to fit, return [0,0] as fit results')
        
        fitr = [0,0]
        fitf = [-1]
        r0 = [0,0]
        r1 = [0,0]
        cov= [r0,r1]
        
    return fitr,fitf,cov