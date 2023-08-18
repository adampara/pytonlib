#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:41:09 2019

@author: para
"""
from ROOT                               import TFile,gDirectory
from histograms_from_file               import ldir    
def fetch_histogram_from_file(file,hist_name):
    """
    fetch a specific fihstogrm form a file
    """

    MyFile = TFile(file)  
    gDirectory.pwd()
    dir = gDirectory
    lhist = ldir(dir,MyFile)

    hst = None
    for h in lhist:

        if h.GetName() == hist_name:
            hst = h.ReadObj()
            hst.SetDirectory(0)
    

    return hst