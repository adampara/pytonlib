#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:56:29 2019

@author: para
"""
from __future__ import division
from __future__ import print_function
from builtins import zip
from builtins import range
from past.utils import old_div
import numpy                as np
import matplotlib.pyplot    as plt
from unpack_histogram       import unpack_histogram

def edit_histogram(hist, new = True, fign=-1, show=True,
                   title = '', label = '',
                   xlow = np.nan, xup = np.nan,
                   rebin=1, norm=False, mark='*',col='', linestyle = 'None',
                   xaxis='NO', yaxis='NO',
                   fsave='NO', bias_y = 0, x_offset=0,
                   flip_x = False, lin_bias = 'NO'):
    """
    add histogram hist to a mathplot plot
    """
    print(lin_bias)
    #   crate new figure, if requested
    if new:  
        if fign < 0:
            plt.figure()      # next figure, if fign<0
        else:
            plt.figure(fign)   # requested figure number
            
    #  get histogram content
    nbin, delta, xbinc, cont, entries= unpack_histogram(hist)
    cont = cont - bias_y
    if lin_bias != 'NO':    #   subtract linearly varying offset
        for i in range(len(cont)):
            bias = lin_bias[0] + lin_bias[1] * xbinc[i]
            cont[i] -= bias
    if norm:
        cont = old_div(cont,entries)
    # apply x limits, if so requested
    if np.isnan(xlow) and np.isnan(xup):
        xbinc_n = xbinc
        cont_n  = cont

    else:
        if np.isnan(xlow): xlow = xbinc[0] - 10.
        if np.isnan(xup) : xup = xbinc[-1] + 10.  
        xbinc_n = []
        cont_n  = []
        
        for x,c in zip(xbinc,cont):
            if x > xlow and x < xup:
                xbinc_n.append(x)
                cont_n .append(c)

    print('rebin = ',rebin)                
    if rebin !=1:
        
        xb = np.array(xbinc_n)
        val = np.array(cont_n)
        
        n_arl = int(old_div(len(xb),rebin))*rebin
        
        xbinc_n = xb[0:n_arl].reshape(-1,rebin).mean(axis=1)
        cont_n = val[0:n_arl].reshape(-1,rebin).mean(axis=1)
    print(type(xbinc_n))
    xbinc_n = np.asarray(xbinc_n)
    xbinc_n = xbinc_n + x_offset       #   shift along x axis
    if flip_x  : xbinc_n = -xbinc_n
    
    args = ['xbinc_n', 'cont_n' ]
    kwargs = {}
    kwargs['linestyle'] = linestyle
    kwargs['marker'] = mark
    if col   != '' : kwargs['c'] = col
    if label != '' : kwargs['label'] = label
    plt.plot(xbinc_n,cont_n,**kwargs)
    
    #plt.plot(xbinc_n,cont_n,label=label,marker=mark)            

    #  use the requested/original or NO title
    if title == '':  title = hist.GetTitle() 
    if title != 'NO':  plt.title(title)
    if xaxis != 'NO':  plt.xlabel(xaxis)   
    if yaxis != 'NO':  plt.ylabel(yaxis)   
    if label != '': plt.legend()

    if fsave !='NO': plt.savefig(fsave)
    if show: plt.show()
            