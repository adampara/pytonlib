#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:06:21 2019

@author: para
"""

def get_2D_bin_content(hst,xv,yv):
    """
    get bin content of 2d hstogram
    """
    
    ixb = hst.GetXaxis().FindBin(xv)
    iyb = hst.GetYaxis().FindBin(yv)
    
    return hst.GetBinContent(ixb,iyb)
