#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:44:33 2019

@author: para
"""
from __future__ import print_function

import matplotlib.pyplot       as plt

def make_frame(nbinx, nbiny, title='',d_beg='',d_end='',ylow='',yup='',maxticks='',dates = False):
    """
    set a frmame with nbny (horizothal) and nbinx (vertical) plots
    """

    aax = (1,) * nbinx
    ax = (aax,) * nbiny

    f, (ax) = plt.subplots(nbinx,nbiny, sharex=True, sharey=True)
    f.suptitle(title)
    
    f.subplots_adjust(hspace=0.05)
    f.subplots_adjust(wspace=0.05)
    f.subplots_adjust(top=0.95)
    f.subplots_adjust(right=0.95)
    f.subplots_adjust(left=0.05)  
    if dates:
        f.autofmt_xdate(bottom=0.1, rotation=90, ha='right') 

    #   --- customize x and y range and number of ticks

    if nbinx==1 and nbiny==1:
        ax = [[ax]]   # cast ax into an array to make the operations consistent
    if d_beg != '' and d_end != '':
        for axx in ax:

            dlim = [d_beg,d_end]
            for axxx in axx:
                axxx.set_autoscalex_on(False)
                axxx.set_xlim(dlim)

    if ylow != '' and yup != '':
        print(' setting up y scale  ',ylow,yup, title)
        for axx in ax:

            ylim = [ylow,yup]
            for axxx in axx:
                axxx.set_ylim(ylim)  

    if maxticks != '':
        for axx in ax:
            for axxx in axx:                 
                axxx.xaxis.set_major_locator(plt.MaxNLocator(maxticks))
                
    #for a single frame ax is a scalar. put it back..               
    if nbinx==1 and nbiny==1:
        ax = ax[0][0]               
    return f,(ax)

