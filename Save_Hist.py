
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:43:14 2017

@author: para
"""

from ROOT import gDirectory

def Save_Hist(lhist, hist_file, delete=False):
    """
    Store histograms in a lhist list to a file
    if lhist is empty save all histograms in memory
    Jan 4 2019: allow for some of the entries to be  dictionaries of histograms
    Wed Aug 24 20:44:39 CDT 2022:  add delete option
    """
    from ROOT import TFile

    if len(lhist) == 0:
        gDirectory.cd()
        lhist = gDirectory.GetList() 
        

    fr = TFile(hist_file, 'recreate')

    #   support: 
    #         list of histograms  
    #         list of dictionaries of hstograms
    #         list of lists of histograms         
    for h in lhist:

        if type(h) is dict:
            for item in h:
                h[item].Write()
                if delete:  h[item].Delete()
        elif type(h) is list:
            for hh in h:
                if type(hh) is list:
                    for hhh in hh:
                        hhh.Write()
                        if delete:  hhh.Delete()
                else:                        
                    hh.Write()
                    if delete:  hh.Delete()
        else:
            h.Write()
            if delete:  h.Delete()
    fr.Close()
