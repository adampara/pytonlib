#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:49:53 2020

@author: para

ROOT utilities

"""

from ROOT                 import TFile


def fetch_histogram_from_file(fname, hname):

    """
    fetch object from ROOT file
    """
    
    fp = TFile(fname)
    h  = fp.Get(hname)
    h.SetDirectory(0)
    
    return h

def list_histograms_in_file(fname):

    """
    print directory of a ROOT file
    """
    
    fp = TFile(fname)
    fp.ls()
        
        
