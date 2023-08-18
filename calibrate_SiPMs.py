#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:58:39 2018

@author: para
"""
from __future__ import print_function

from builtins import range
from ROOT                import TH1F
import matplotlib.pyplot as plt
import numpy             as np
from char_sipm           import char_sipm
from plot_histogram      import plot_histogram

def calibrate_SiPMs(sipmwf, nsipm, maxev, calibrate=False, debug=False):
    """
    find pedestal and sigma nd single pe vaue fromthe distribution of thw waveform values
    """
    
    name = '--->  calibrate_SiPMs: '
     
    ped     = {}
    sigped  = {}
    spe     = {}

    single_pe_def = 15.
    min_val_allow = 3. 
    max_val_allow = 30.    
    title = 'SiPM channels'
    val_sipm = TH1F(title,title,256,0.5,256.5)
        
    for sipm in range(nsipm):

        if calibrate :        
            val_sipm.Reset()

                           
            for iev in range(maxev):
    
                nzi = np.nonzero(sipmwf[sipm][iev])[0]         # indices on non-zero elements
                nz = sipmwf[sipm][iev][nzi] 
                #print 'event ',iev, 'sipm ',sipm  ,'   length of nz ',len(nz) 
                for val in nz:
                    val_sipm.Fill(val)                    
     
    
            ped[sipm],sigped[sipm],spe[sipm] = char_sipm(val_sipm,  debug=debug)
            print(name,'  sipm ',sipm, '  pedestal  ',ped[sipm], '  sigma ', sigped[sipm],  'spe  ',spe[sipm])
            if spe[sipm] < min_val_allow or spe[sipm] > max_val_allow or spe[sipm] ==13.0 :
                print('   SiPM  ',sipm, ' single pe value out of range ', spe[sipm])
                #plot_histogram(val_sipm)  

        else:  
            
            #   approximate calibration for debugging and code development
            
            ped[sipm] = 50.
            spe[sipm] = single_pe_def
            sigped[sipm] = 1.5   

    return ped,sigped,spe
            
 