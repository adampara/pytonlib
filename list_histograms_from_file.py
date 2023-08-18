#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:41:09 2019

@author: para
"""
from __future__ import print_function
from ROOT                               import TFile,gDirectory
from histograms_from_file               import ldir    
def list_histograms_from_file(h_file):
    """
    print list of histograms in a file
    """

    MyFile = TFile(h_file)  
    gDirectory.pwd()
    dir = gDirectory
    lhist = ldir(dir,MyFile)

    print('histograms from file ', h_file)
    
    for h in lhist:
        print("{:>10} {:>40}".format(h.GetClassName(), h.GetName()))

def get_list_of_histograms_from_file(h_file, debug=False):
    """
    return list of histograms in a file
    Wed Oct 12 15:49:33 CDT 2022
    commented out gDirectory.pwd() to avoid the unnecessary output line
     
    """

    MyFile = TFile(h_file) 
    

    #gDirectory.pwd()

    dir = gDirectory

    lhist = ldir(dir,MyFile)

    h_Type = []
    h_Name = []    
    for h in lhist:
        if debug: print("{:>10} {:>40}".format(h.GetClassName(), h.GetName()))
        h_Type.append(h.GetClassName())
        h_Name.append(h.GetName())
        
    return h_Type, h_Name