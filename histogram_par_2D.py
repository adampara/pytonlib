#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:11:08 2020

@author: para
"""

def histogram_par_2D(hh):
    """
    fetch 2d histogram characteristics
    """
    
    nbinx = hh.GetNbinsX()
    nbiny = hh.GetNbinsY()
 
    xmin = hh.GetXaxis().GetBinLowEdge(1)
    ymin = hh.GetYaxis().GetBinLowEdge(1)
    
    binx = hh.GetXaxis().GetBinWidth(1)
    biny = hh.GetXaxis().GetBinWidth(1)
    
    xmax = xmin + nbinx * binx
    ymax = ymin + nbiny * biny
    
    return nbinx, xmin, xmax, binx, nbiny, ymin, ymax, biny