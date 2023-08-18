#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:53:59 2018

@author: para
"""

from builtins import range
from ROOT import TH1F
from plot_histogram import plot_histogram

def array_to_histogram(ar, title = ' ', book=True, plot=False):
    """
    display array as root histogram
    if Book = False the histogram is already existing and fill ot with the vakyes of the array
    """
    
    nbins = len(ar)

    if book:
        
        hist = TH1F(title,title,nbins,-0.5,nbins+0.5)
    else:
        hist = title
        
    for i in range(nbins):
        hist.SetBinContent(i+1,ar[i])
        hist.SetBinError(i+1,0.)
        
    if plot:        
        plot_histogram(hist)    
        hist.Delete()

    if book:        
        return hist