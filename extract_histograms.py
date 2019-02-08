#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:41:30 2017

@author: para
"""
from ROOT import TFile, gDirectory
from histograms_from_file import ldir



def extract_histograms(filelist,h_to_save,str1,str2,tit='waveform, Run ',debug=False):
    """
    from a set of files extract requested histogram
    [for now] assume that the filenames contain the run number
    enclosed by str1 and str2
    """
    wf_hist = []
    
    for fi in filelist:
        if debug:
            print 'Extract histograms from file ',fi
            print '  str1 = ',str1, 'str2 = ',str2, '  h_to_save =  ',h_to_save
        tokens = fi.split(str1)
        run = tokens[1].split(str2)[0]
 
        MyFile = TFile(fi)  
        gDirectory.pwd()
        dir = gDirectory
        lhist = ldir(dir,MyFile,debug=False)
        
        #   lhist is a list of all histograms in a file
        
        for hist in lhist:
            if debug:
                print ' examine histogram  ',hist.GetName()
            if h_to_save == hist.GetName() or h_to_save == '*':
                hh = hist.ReadObj()
                if h_to_save == '*':
                    title = hh.GetTitle() + '_' + run
                else:
                    title = h_to_save + '_' +  run
                if debug:
                    print '   save histogram ',hist.GetName(), ' with title ',title
                ev_hist = hh.Clone()
                ev_hist.SetTitle(title)
                ev_hist.SetDirectory(0)
                wf_hist.append((run,ev_hist))
    return wf_hist
