#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:47:45 2022

@author: para
"""

import tables            as tb
import pandas            as pd
import copy

def load_wfms_df_chunk(filename, kind, part, chunk = 50):
    """
    load waveforms (raw or BLR corrected, depending on 'kind') and event information from the waveforms file
    read data file in chunks 
    return OK = False if no data in a requested chunk
    
    """

    beg = (part -1) * chunk
    end = beg + chunk
    #    will return section beg to end

    OK   = False
    wave = None
    sipm = None
    evno = None
    
    with tb.open_file(filename, 'r') as h5f:
        to_df = pd.DataFrame.from_records
 
        evwf = h5f.root.Run.events.read()
        
        if len(evwf) -1 > beg: 
            OK = True
            end = min(end,len(evwf)+1)
            
            aux = copy.copy(evwf[beg:end])
            evno = to_df(aux)
            del evwf

            
            wf = h5f.root.RD
            stwf = wf.sipmrwf[beg:end]
            sipm = to_df(stwf)


           
            if kind == 'cwf':
    
                wf = h5f.root.BLR
                wfm = wf.pmtcwf[beg:end]
                wave = to_df(wfm)
                
            if kind == 'rwf':
                
                wf = h5f.root.RD  
                twf = wf.pmtrwf[beg:end]                
                wave = to_df(twf)

       
    return wave,sipm,evno,OK