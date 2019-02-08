#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:43:14 2017

@author: para
"""

from ROOT import gDirectory

def Save_Hist(lhist,hist_file):
    """
    Store histograms in a lhist list to a file
    if lhist is empty save all histograms in memory
    Jan 4 2019: allow for some of the entries to be  dictionaries of histograms
    """
    from ROOT import TFile

    if len(lhist) == 0:
        gDirectory.cd()
        lhist = gDirectory.GetList() 
        

    fr = TFile(hist_file, 'recreate')
            
    for h in lhist:

        if type(h) is dict:
            for item in h:
                h[item].Write()
        else:
            h.Write()
    fr.Close()
