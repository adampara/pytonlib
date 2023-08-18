
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:52:36 2019

@author: para
"""
from __future__ import division
from __future__ import print_function

from builtins import range
from past.utils import old_div
from unpack_histogram       import unpack_histogram

def divide_2d_by_1D_histograms(H2D,H1D):
    """
    normalize the H2D(ix,iy) to H2(ix,iy)/H1d(ix)
    """
    
    nbin,delta,xc,cont,noent = unpack_histogram(H1D)
    
    nbinx = H2D.GetNbinsX()
    nbiny = H2D.GetNbinsY()
    
    if nbin != nbinx:
        print(' inconsistemt histograms', H2D, H1D)
        exit()
        
    for ix in range(nbinx):
        for iy in range(nbiny):
            val = H2D.GetBinContent(ix+1,iy+1)
            if val !=0 : val = old_div(val,cont[ix])
            H2D.SetBinContent(ix+1,iy+1,val)
    