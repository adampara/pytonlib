#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:59:25 2018

@author: para
"""
from plot_histogram import plot_histogram

def char_sipm(hist,fun='gaus',min_entries=1000,xl=40,xu=60,debug=False):
    """ 
    derive charactristics of the SiPM from the values histogram
    """
    
    #   default va;ues for SiPMs which do not have enough data or fail the fit

    name = '  ------->  char_sipm:'    
    ped = 50
    spe = 13
    sigped = 100
       
    n_entries = hist.GetEntries()
    
    if n_entries<min_entries:
        print name, 'Not enugh data  , nentries = ',n_entries, '  return defaults vaalues'
    else:
        
        fit_res = hist.Fit(fun,'SQ0','',xl,xu) 
        if fit_res.Status() == 0:
            ped =  fit_res.Parameter(1)
            sigped =  fit_res.Parameter(2)
            
            if debug:
                print name, 'Fit results ',fit_res
                #plot_histogram(hist)
                
            n_sig = 3
            xl = fit_res.Parameter(1) + (n_sig + 1.0) *( max(fit_res.Parameter(2),2.))
            xu = fit_res.Parameter(1) + 3.5 * n_sig * ( max(fit_res.Parameter(2),2.))
            fit_res = hist.Fit(fun,'SQ0','',xl,xu) 
    
            if int(fit_res) == 0:
                spe = fit_res.Parameter(1) - ped
            
            if debug:
                
                print name, 'Fit results ',ped,sigped,spe
                plot_histogram(hist)  
            
    return ped,sigped,spe