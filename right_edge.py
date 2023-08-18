#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:38:03 2018

@author: para
"""
from __future__ import print_function
from builtins import range
from smooth_wave import smooth_wave
import matplotlib.pyplot as plt

def right_edge(wave, cut=200, cutb=30, nauxb=200, nauxe=5, reverse=True, debug=False):
    """
    find end of the pulse scanning backward
    find position of high threshold (cut) and extend to the position of lower threshold (cutb)
    in the small neighbourhood (nauxb)
    """

    name = '   ---> right_edge: '
    nend = len(wave) 
    if reverse:
        reversed_arr = wave[::-1]
        thrc = (reversed_arr > cut).argmax() if (reversed_arr > cut).any() else -1
        aux = reversed_arr[thrc-nauxb:thrc+nauxe]
        thrb = (aux > cutb).argmax() if (aux > cutb).any() else -1
        nmax = nend - thrc - thrb + nauxb  
        
    else:

        thrc = (wave > cut).argmax() if (wave > cut).any() else -1
        naux = min(nauxb,0)
        aux = wave[thrc-naux:thrc+nauxe]
        thrb = (aux > cutb).argmax() if (aux > cutb).any() else -1
        nmax = thrc + thrb - naux
        

    if debug:
        print(name,' length of the waveform  ',nend, ' thrc = ',thrc,' thrb = ', thrb, 'nmax= ',nmax)
        
    return nmax

def right_edge_new(waveform,cut=100, cutb=20, nbelow= 2000, ntrigger=25000, nsmooth=10, debug=False):
    """ 
    define the end of the pulse when the pulse dips below the cutb value for at least nbelow samples
    the main pulse begins when the waveform crosses cut value after 'trigger' position
    """

    name = '  ---->  right_edge_new : '    
    wave = smooth_wave(waveform,nsmooth)
    
    next_pulse_beg = ntrigger
    pulse_end = 0
    
    while next_pulse_beg > pulse_end:    
        pulse_beg = right_edge(wave[next_pulse_beg:], cut=cut, reverse=False, debug=debug) + next_pulse_beg
        pulse_end = right_edge(-wave[pulse_beg:],cut=-cutb,cutb=-cutb,reverse=False,debug=debug) + pulse_beg
        next_pulse_beg = right_edge(wave[pulse_end:],cut=cut,reverse=False) + pulse_end 

    if debug:
        print(name,' pulse_beg = ',pulse_beg, 'pulse_end ',pulse_end, ' next_pulse_beg = ',next_pulse_beg)
        plt.figure()
        plt.plot(waveform)
        plt.plot(wave)
        plt.title(name)
        plt.show()
        
    return pulse_end        

def right_edge_new_new(waveform,cut=50, cutb=20, nbelow= 2000, ntrigger=25000, nsmooth=5, debug=False):
    """ 
    define the end of the pulse when the pulse dips below the cutb value for at least nbelow samples
    the main pulse begins when the waveform crosses cut value after 'trigger' position
    """

    name = '  ---->  right_edge_new_new : '    
    wave = smooth_wave(waveform[ntrigger:],nsmooth)
    #wave = waveform[ntrigger:]
    keep_doing = True
    found_beg = False
    nlow = 0
    curr = 0
    high = False
    found_drop = False
    done = False
    pulse_end = -1
    pulse_beg = -1
#    while keep_doing:
#        
#
#        curr += 1

#    for curr in range(len(waveform)-ntrigger):
    for curr in range(len(wave)):
        if done: break
        val = wave[curr]
#        val = waveform[ntrigger+curr]
        
        if found_beg:
            #  inside the pulse, if still above cutb keep going
            if val > cutb: 
                high = True
                found_drop = False
            else:
                high = False
                if found_drop:
                    nlow +=1
                    if nlow > nbelow: keep_doing = False
                    done = True
                else:
                    nlow = 1
                    found_drop = True
                    pulse_end = curr
                    
        
            
        else:
            if val > cut:       # beginning of the pulse found
                found_beg = True
                pulse_beg = curr
                high = True
 
        if debug: print(name, 'current pointer ',curr,'  value  ',val,'  found_beg ',found_beg,'  high = ',high,'  found_drop = ',found_drop, 'nlow ', nlow, ' keep_doing ', keep_doing)

    if pulse_beg > 0:
            
        pulse_end += ntrigger
        pulse_beg += ntrigger
        
    else:
        #   no pulse beginning found at the current threshold
        print('  no ulse found with the threshold of ', cut, 'return pulse_end = 0')
        pulse_end = 0
        
    if debug:
        print(name,' pulse_beg = ',pulse_beg, 'pulse_end ',pulse_end)
        plt.figure()
        plt.plot(waveform)
        plt.plot(wave)      #  does not work properly with wave smoothed out only beyond triger position. Needs fixing
        plt.title(name)
        plt.show()
        
    return pulse_end        
