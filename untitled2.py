#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:36:20 2018

@author: para
"""

def load_wfms_df(filename, kind):
    """
    load waveforms (raw or BLR corrected, depending on 'kind') and event information from the waveforms file
    """
    
    with tb.open_file(filename, 'r') as h5f:
        to_df = pd.DataFrame.from_records
        
        if kind == 'cwf':

            wf = h5f.root.BLR
            wave = to_df(wf.pmtrwf.read())

        if kind == 'rwf':
            
            wf = h5f.root.RD
            wave = to_df(wf.pmtcwf.read())
                        
            
        evno = to_df(h5f.root.Run.events.read())
        sipm = to_df(wf.sipmrwf.read())
        
    return wave,sipm,evno