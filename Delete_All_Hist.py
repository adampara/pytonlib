#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:43:14 2017

@author: para
"""

from ROOT import gDirectory

def Delete_All_Hist(lhist):
    """
    Delete histograms in a lhist list to a file
    if lhist is empty save all histograms in memory
    Jan 4 2019: allow for some of the entries to be  dictionaries of histograms
    """


    if len(lhist) == 0:
        gDirectory.cd()
        lhist = gDirectory.GetList() 
        



    #   support: 
    #         list of histograms  
    #         list of dictionaries of hstograms
    #         list of lists of histograms         
    for h in lhist:

        if type(h) is dict:
            for item in h:
                h[item].Delete()
        elif type(h) is list:
            for hh in h:
                if type(hh) is list:
                    for hhh in hh:
                        hhh.Delete()
                else:                        
                    hh.Delete()
        else:
            h.Delete()

