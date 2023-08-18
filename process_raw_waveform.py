#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:17:52 2018

@author: para
"""
from __future__ import print_function

from determine_pedestal import determine_pedestal
from improve_pedestal import improve_pedestal
from correct_saturation import correct_saturation, correct_saturation_v2
from correct_saturation import correct_saturation, correct_saturation_v1
from check_time import check_time
from FFT_ped import FFT_ped
import numpy as np

def process_raw_waveform(wave, pmt, iev, tau, lped, accept= 0.1, debug = False, tim_lev=0):
    """
    process raw waveform, deconvolute, etc..
    """
 
    name = '        ---->  process_raw_waveform: '
    tim_lev_cut = 1
#
#    if tim_lev > tim_lev_cut: check_time(name,'  start pedestal  ')    
#    ped = determine_pedestal(wave[pmt][iev], debug=False, title='Event '+str(iev)+' PMT '+str(pmt))
#    wave_zero = -(wave[pmt][iev] - ped)       # invert the waveform
#    #     --- from here on signal is positive
#    if tim_lev > tim_lev_cut: check_time(name,'  improve pedestal  ')  
#    
#    ped_n = improve_pedestal(wave_zero[0:lped], debug=False)  
#    wave_fin = wave_zero - ped_n     
#               #   pedestal corrected raw waveform  
          
    if tim_lev > tim_lev_cut: check_time(name,'  FFT pedestal  ')  
#
    ped = FFT_ped(wave[pmt][iev])    # invert the wavefprm, signals will be positive
    if debug:
        print(name, '  depestal value ',ped)
    wave_fin = -(wave[pmt][iev] - ped)     
    if tim_lev > tim_lev_cut: check_time(name,'  FFT pedestal done ')  
    
    if tim_lev > tim_lev_cut: check_time(name,'  start deconvolution  ')        
    stat,bs,wf_corr_fin,pulse_end = correct_saturation(wave_fin, tau[pmt], accept=accept, debug=debug, tim_lev=tim_lev)  

    if tim_lev > tim_lev_cut: check_time(name,'  end ') 
     
    return wf_corr_fin, pulse_end

def process_raw_waveform_v2(wave, tau, lped, accept= 0.1, S2_beg=640, S2_end=670, valcut=30,  debug = False, tim_lev=0):
    """
    process raw waveform, deconvolute, etc..
    use external timing info from SiPM
    if baseline shift greater than 'accept' try to corerct the wavefprm assuming saturation
    if S2 too close to the beginning use the entire waveform to determine the pedestal
    tim_level > tim_leve_cut is for the timing studies.
    
    """
 
    name = '        ---->  process_raw_waveform: '
    tim_lev_cut = 1

    #    determine the pedestal value
         
    if tim_lev > tim_lev_cut: check_time(name,'  FFT pedestal  ')  
    #   if S2 pulse too close to the beginning of the waveform try to use the entire waveform to determinethe pedestal
    if S2_beg > 100:
        ped = FFT_ped(wave[0:S2_beg]) 
    else:
        ped = FFT_ped(wave)
        
    #    invert the polarity
    
    wave_fin = -(wave - ped)    # invert the waveform, signals will be positive
    if tim_lev > tim_lev_cut: check_time(name,'  FFT pedestal done ')  

    #   if there are no big pulses the BLR correction is unnecessary and introduces unnecessary errors   
    maxval = np.max(wave_fin)
    if maxval > valcut:
        
        if tim_lev > tim_lev_cut: check_time(name,'  start deconvolution  ')        
        stat,bs,wf_corr_fin = correct_saturation_v2(wave_fin, tau, S2_beg=S2_beg, S2_end=S2_end, accept=accept, debug=debug, tim_lev=tim_lev)  
    
        if tim_lev > tim_lev_cut: check_time(name,'  end ') 
     
        blr_shift_cut = 5.
        if abs(stat) < blr_shift_cut:
            good = True
        else:
            good = False
    else:
        good = True
        wf_corr_fin = wave_fin
            
    return good,wf_corr_fin


def process_raw_waveform_v1(wave, tau, lped,  S2_beg=640, valcut=30):
    """
    process raw waveform, deconvolute, etc..
    use external timing info from SiPM
    if baseline shift greater than 'accept' try to corerct the wavefprm assuming saturation
    if S2 too close to the beginning use the entire waveform to determine the pedestal
    
    """

    #   if S2 pulse too close to the beginning of the waveform try to use the entire waveform to determinethe pedestal
    if S2_beg > 100:
        ped = FFT_ped(wave[0:S2_beg]) 
    else:
        ped = FFT_ped(wave)
        
    wave_fin = -(wave - ped)    # invert the waveform, signals will be positive
    
    #   if there are no big pulses the BLR correction is unnecessary and introduces unnecessary errors   
    maxval = np.max(wave_fin)
    good = True
    
    if maxval > valcut:
              
        wf_corr_fin = correct_saturation_v1(wave_fin, tau)  

    else:

        wf_corr_fin = wave_fin
            
    return good,wf_corr_fin