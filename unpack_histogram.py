#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:35:45 2017

@author: para
"""
from __future__ import print_function

from builtins import range
import numpy as np

def unpack_histogram(h, debug=False):
    """
    unpack 1D histogram
    """
    
    if debug:
        print('unpack histogram ', h.GetName())
    
    # extract information about the histogram
    nbin = h.GetNbinsX()
    xc   = np.zeros(nbin)
    cont = np.zeros(nbin)
    for bin in range(nbin):
        xc[bin] = h.GetBinCenter(bin+1)
        cont[bin] = h.GetBinContent(bin+1)
    delta = xc[1] - xc[0]       #  binning

    return nbin,delta,xc,cont,h.GetEntries()

def unpack_histogram_error(h, debug=False):
    """
    unpack 1D histogram with errors
    """
    
    if debug:
        print('unpack histogram ', h.GetName())
    
    # extract information about the histogram
    nbin = h.GetNbinsX()
    
    xc   = np.zeros(nbin)
    cont = np.zeros(nbin)
    err  = np.zeros(nbin)
    
    for bin in range(nbin):
        xc   [bin]   = h.GetBinCenter (bin+1)
        cont [bin]   = h.GetBinContent(bin+1)
        err  [bin]   = h.GetBinError  (bin+1)
        
    delta = xc[1] - xc[0]       # binning

    return nbin,delta,xc,cont,err,h.GetEntries()

def offset_histogram(h, offset, debug=False):
    """
    add offset to all bins of  1D histogram
    """
    
    if debug:
        print('unpack histogram ', h.GetName())
    
    # extract information about the histogram
    nbin = h.GetNbinsX()

    for bin in range(nbin):
        cont = h.GetBinContent(bin+1) + offset
        h.SetBinContent(bin+1, cont)        

def integrate_density_histogram(h, debug=False):
    """
    replace conent of a histogram by x*h(x)
    """
    
    if debug:
        print('integrate density histogram ', h.GetName())
    
    # extract information about the histogram
    nbin = h.GetNbinsX()

    for bin in range(nbin):
        xc    = h.GetBinCenter (bin+1)
        cont  = h.GetBinContent(bin+1) 
        h.SetBinContent(bin+1, xc * cont)        
