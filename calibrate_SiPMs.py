#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:58:39 2018

@author: para
"""

from ROOT import TH1F
import matplotlib.pyplot as plt
import numpy as np
from char_sipm import char_sipm


def calibrate_SiPMs(sipmwf, nsipm, maxev, calibrate=False, debug=False):
    """
    find pedestal and sigma nd single pe vaue fromthe distribution of thw waveform values
    """
    
    name = '--->  calibrate_SiPMs: '
     
    ped     = {}
    sigped  = {}
    spe     = {}
    
    title = 'SiPM channels'
    val_sipm = TH1F(title,title,256,0.5,256.5)
        
    for sipm in range(nsipm):

        if calibrate :        
            val_sipm.Reset()
            if debug:
                plt.figure(10)
                           
            for iev in range(maxev):
    
                nzi = np.nonzero(sipmwf[sipm][iev])[0]         # indices on non-zero elements
                nz = sipmwf[sipm][iev][nzi] 
                #print 'event ',iev, 'sipm ',sipm  ,'   length of nz ',len(nz) 
                for val in nz:
                    val_sipm.Fill(val)                    
     
    
            ped[sipm],sigped[sipm],spe[sipm] = char_sipm(val_sipm,  debug=False)
            print name,'  sipm ',sipm, '  pedestal  ',ped[sipm], '  sigma ', sigped[sipm],  'spe  ',spe[sipm]
            #plot_histogram(val_sipm)  
            if debug:
     
                plt.plot(nzi,nz-ped[sipm])  
                plt.title('Event ' + str(iev) + '  Sipm ' + str(sipm))
                plt.show()
        else:  
            
            #   approximate calibration for debugging and code development
            
            ped[sipm] = 50.
            spe[sipm] = 13.
            sigped[sipm] = 1.5   

    return ped,sigped,spe
            
 