#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:27:45 2022

@author: para
"""
from unpack_histogram      import unpack_histogram

def overlay_and_shift_histogram(hist, n_pieces, delta):
    """
    overlay n_pieces of the histogram, shifted by delta   

    """
    hist_o = hist.Clone()
    hist_o.SetTitle(hist.GetTitle() + ' , ' + str(n_pieces) + ' copies shifted by ' + str(delta))

    hist_o.Reset()
    
    nbin,dx,xc,cont,entries = unpack_histogram(hist) 
    
    for piece in range(n_pieces):
        delay = piece * delta
        for i in range(len(cont)):
            hist_o.Fill(xc[i] + delay,cont[i])

    return hist_o   