#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:21:59 2018

@author: para
"""
from __future__ import division
from __future__ import print_function
from past.utils import old_div
import numpy as np
from right_edge import right_edge, right_edge_new, right_edge_new_new
from peak_in_waveform import peak_in_waveform
from math import exp
from saturation_corr import saturation_corr
import matplotlib.pyplot as plt
from ac_coupl import ac_coupl
from check_time import check_time
from FFT_ped import FFT_ped

def correct_saturation( wave_fin, tau, accept=0.1, debug=False, tim_lev=0):
    
    """
    attempt to correct the saturation: forcing the baseline return by a single correction to the smple with the peak amplitude
    wave_fin is a raw waveform
    this version will identify the 'no signal, region behaind the peak to evaluate the baseline shift
    """

    name = '                          --->  correct_saturation:  '
    tim_lev_cut = 2

    if tim_lev > tim_lev_cut: check_time(name, '  begin  ')    
    if debug: print(name, '  begin')
    wf_corr,bs =  ac_coupl(wave_fin,tau ) 
    if tim_lev > tim_lev_cut: check_time(name, '  deconvoluted  ')  
    
    if debug:

        plt.figure()
        plt.plot(wave_fin)
        plt.plot(wf_corr)
        plt.title('correct saturation, raw and initially deconvoluted')
        plt.show() 
 
    guard = 1000  
     
    max_pos = np.argmax(wf_corr[:-guard])                 
    if debug:
        print(name,'  maximum at the position ',max_pos)
        

    if tim_lev > tim_lev_cut: check_time(name, '  look for long pulses ')  

    pulse_end = right_edge_new_new(wf_corr[:-guard],cut=50,debug=debug)
    if debug: print(name, 'pulse_end ',pulse_end)
    if tim_lev > tim_lev_cut: check_time(name, '  pulses characterized  ')  
    
    if debug:
        print(name,'  pulse end ',pulse_end)

    stat,bl_shift = peak_in_waveform(wf_corr[pulse_end:pulse_end+1000],debug=False) 
    if tim_lev > tim_lev_cut: check_time(name, '  baseline shift determined ')  
    
    if debug or stat != 0:
        print('  correct_saturation  :  initial  -bl_shift, stat  ', bl_shift, stat)

    if abs(bl_shift) > accept or stat !=0:    #  small baseline shift  or catastrophic fiure   
        
        x1 = 0
        y1 = bl_shift
        satur_c = old_div(bl_shift * exp(tau*(pulse_end + 500 - max_pos)),tau) 
    
        if debug:
            print(name, ' position of the maximum, end of the pulse ',max_pos, pulse_end)
            print(name, '  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c)
        sh0 = - 0.3 * satur_c
        stat,bs0,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh0,tau) 

        x2 = sh0
        y2 = bs0     
        if bs0*bl_shift < 0:

            pass            # baseline shift changed sign, will iterpolate
        else:

            sh1 = 0.1*sh0
            stat,bs1,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh1,tau) 
            y2 = bs1
            x2 = sh1
            
            if bl_shift*bs1<0:
                pass
            else:

                niter = 0
                nit_max = 5
                
                while stat != 0 and niter<nit_max:
                    sh1 = 0.5*sh1
                    stat,bs1,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh1,tau)
                    niter += 1
                y2 = bs1
                x2 = sh1   

        a = old_div((y2-y1),(x2-x1))
        b = y1 - a*x1
        shift = old_div(-b,a)
           
        stat,bs,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,shift,tau) 
        if debug:
            print(name,'  final correction of the waveform  ',shift)
            print('  correct_saturation  :  position of the maximum, end of the pulse ',max_pos, pulse_end)
            print('  correct_saturation  :  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c)

    else:
        bs=bl_shift
        wf_corr_s = wf_corr
        
    if debug:   
        plt.figure()
        plt.plot(wave_fin)
        plt.plot(wf_corr_s)
        plt.plot(wf_corr)
        plt.title('correct_saturation, original and final waveforms')
        plt.show()
    if tim_lev > tim_lev_cut: check_time(name, '  baseline shift optimized ')    
   
    return stat,bs,wf_corr_s,pulse_end
           
def correct_saturation_old( wave_fin, tau, accept=0.5, debug=False):
    
    """
    attempt to correct the saturation: forcing the baseline return by a single correction to the smple with the peak amplitude
    wve_fi is a raw waveform
    this is an initial version trying to use the entire waveform to the right of the 'peak'
    """

    name = '   --->  correct_saturation:  '
    wf_corr,bs =  ac_coupl(wave_fin,tau ) 

    if debug:

        plt.figure()
        plt.plot(wave_fin)
        plt.plot(wf_corr)
        plt.title('correct saturation, raw and initially deconvoluted')
        plt.show() 
        
    max_pos = np.argmax(wf_corr)                 
    pulse_end = right_edge(wf_corr,cut=50,debug=debug)

    stat,bl_shift = peak_in_waveform(wf_corr[pulse_end:pulse_end+1000],debug=False) 

    if abs(bl_shift) > accept:      
        satur_c = old_div(bl_shift * exp(tau*(pulse_end + 500 - max_pos)),tau) 
    
        if debug:
            print(name, ' position of the maximum, end of the pulse ',max_pos, pulse_end)
            print(name, '  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c)
        sh0 = - 0.3 * satur_c
        stat,bs0,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh0,tau) 
     
        if bs0*bl_shift < 0:
            pass
        else:
            if abs(bs0)<abs(bl_shift):
                step = abs(bl_shift)-abs(bs0)
                nstep = 1 + old_div(abs(bl_shift),step)
                sh1 = sh0 * nstep
                stat,bs1,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh1,tau) 
                if bl_shift*bs1<0:
                    bs0 = bs1
                    sh0 = sh1
                else:
                    print('correct saturation: odd.. should not have reached that')
                    print('  correct_saturation  :  position of the maximum, end of the pulse ',max_pos, pulse_end)
                    print('  correct_saturation  :  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c)
 
                    plt.figure()
                    plt.plot(wave_fin)
                    plt.plot(wf_corr_s)
                    plt.plot(wf_corr)
                    plt.title('corerct_saturation, original and final waveforms')
                    plt.show()
    
        a = old_div((bl_shift-bs0),(0-sh0))
        b = bs0 - a*sh0
        shift = old_div(-b,a)
    
                
        stat,bs,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,shift,tau) 
        if debug:
            print('  correct_saturation  :  position of the maximum, end of the pulse ',max_pos, pulse_end)
            print('  correct_saturation  :  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c)

    else:
        bs=bl_shift
        wf_corr_s = wf_corr
        
    if debug:   
        plt.figure()
        plt.plot(wave_fin)
        plt.plot(wf_corr_s)
        plt.plot(wf_corr)
        plt.title('corerct_saturation, original and final waveforms')
        plt.show()
        
    return stat,bs,wf_corr_s
 
def correct_saturation_v2( wave_fin, tau, accept=0.1, S2_beg=640, S2_end=660, debug=False, tim_lev=0):
    
    """
    attempt to correct the saturation: forcing the baseline return by a single correction to the smple with the peak amplitude
    wave_fin is a raw waveform
    this version will identify the 'no signal, region behaind the peak to evaluate the baseline shift
    """

    name = '                          --->  correct_saturation_v2:  '
    tim_lev_cut = 2
    if debug: print(name, '  begin')
    
    if tim_lev > tim_lev_cut: check_time(name, '  begin  ')    
    wf_corr,bs =  ac_coupl(wave_fin,tau ) 
    if tim_lev > tim_lev_cut: check_time(name, '  deconvoluted  ')  
    
    if debug:

        plt.figure()
        plt.plot(wave_fin)
        plt.plot(wf_corr)
        plt.title('correct saturation, raw and initially deconvoluted')
        plt.show() 
 
    guard = 1000
     
#    max_pos = np.argmax(wf_corr[:-guard])                 
#    if debug:
#        print name,'  maximum at the position ',max_pos
#        
#
#    if tim_lev > tim_lev_cut: check_time(name, '  look for long pulses ')  
#
#    pulse_end = right_edge_new_new(wf_corr[:-guard],cut=50,debug=debug)
#    if debug: print name, 'pulse_end ',pulse_end
#    if tim_lev > tim_lev_cut: check_time(name, '  pulses characterized  ')  
#    
#    if debug:
#        print name,'  pulse end ',pulse_end
#    if tim_lev > tim_lev_cut: check_time(name, '  determine baseline shift ') 
#    stat,bl_shift = peak_in_waveform(wf_corr[S2_end+guard:],debug=False) 
    if tim_lev > tim_lev_cut: check_time(name, '  baseline shift determined ')  

    #   if the pulse is at the end of the waveform cannot determine the baseline shift
    if S2_end+guard < len(wf_corr) -100:
        bl_2 = FFT_ped(wf_corr[S2_end+guard:])
    else:
        bl_2 = 0
        
    stat = bl_2      #   for the moment do not attempt any baseline restorations kludges
    
    if tim_lev > tim_lev_cut: check_time(name, '  baseline shift determined 2')  

    if debug:  print(name, 'baseline shifts  ', bl_2  ,'  S2_end  ',S2_end)  

#
#    bl_shift = bl_2
#    stat = 0
    
#    if debug or stat != 0:
#        print '  correct_saturation  :  initial  -bl_shift, stat  ', bl_shift, stat
#
#    if abs(bl_shift) > accept or stat !=0:    #  small baseline shift  or catastrophic fiure   
#        
#        x1 = 0
#        y1 = bl_shift
#        satur_c = bl_shift * exp(tau*(pulse_end + 500 - max_pos))/tau 
#    
#        if debug:
#            print name, ' position of the maximum, end of the pulse ',max_pos, pulse_end
#            print name, '  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c
#        sh0 = - 0.3 * satur_c
#        stat,bs0,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh0,tau) 
#
#        x2 = sh0
#        y2 = bs0     
#        if bs0*bl_shift < 0:
#
#            pass            # baseline shift changed sign, will iterpolate
#        else:
#
#            sh1 = 0.1*sh0
#            stat,bs1,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh1,tau) 
#            y2 = bs1
#            x2 = sh1
#            
#            if bl_shift*bs1<0:
#                pass
#            else:
#
#                niter = 0
#                nit_max = 5
#                
#                while stat != 0 and niter<nit_max:
#                    sh1 = 0.5*sh1
#                    stat,bs1,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,sh1,tau)
#                    niter += 1
#                y2 = bs1
#                x2 = sh1   
#
#        a = (y2-y1)/(x2-x1)
#        b = y1 - a*x1
#        shift = -b/a
#           
#        stat,bs,wf_corr_s = saturation_corr(wave_fin,max_pos,pulse_end,shift,tau) 
#        if debug:
#            print name,'  final correction of the waveform  ',shift
#            print '  correct_saturation  :  position of the maximum, end of the pulse ',max_pos, pulse_end
#            print '  correct_saturation  :  bl_shift, stat, satur_c  ', bl_shift, stat, satur_c
#
#    else:
#        bs=bl_shift
#        wf_corr_s = wf_corr
#        
#    if debug:   
#        plt.figure()
#        plt.plot(wave_fin)
#        plt.plot(wf_corr_s)
#        plt.plot(wf_corr)
#        plt.title('correct_saturation, original and final waveforms')
#        plt.show()
#    if tim_lev > tim_lev_cut: check_time(name, '  baseline shift optimized ')    
   
    return stat,bs,wf_corr     

def correct_saturation_v1( wave_fin, tau):
    
    """
    Deconvolution only
    """

   
    wf_corr,bs =  ac_coupl(wave_fin,tau ) 
  
    return wf_corr     