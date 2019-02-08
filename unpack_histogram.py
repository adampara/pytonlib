#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:35:45 2017

@author: para
"""

import numpy as np

def unpack_histogram(h, debug=False):
    """
    process a single waveform froma root histograam
    """
    
    if debug:
        print 'unpack histogram ', h.GetName()
    
    # extract information about the histogram
    nbin = h.GetNbinsX()
    xc = np.zeros(nbin)
    cont = np.zeros(nbin)
    for bin in range(nbin):
        xc[bin] = h.GetBinCenter(bin+1)
        cont[bin] = h.GetBinContent(bin+1)
    delta = xc[1] - xc[0]       # time binning

    return nbin,delta,xc,cont,h.GetEntries()

