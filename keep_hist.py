#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:09:17 2018

@author: para
"""

from ROOT import gDirectory

def keep_hist(lhist):
    """
    update list of histograms to keep
    by adding all new existing histograms
    """    

    gDirectory.cd()
    for h in gDirectory.GetList():
        lhist.add(h)       