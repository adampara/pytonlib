#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:37:24 2018

@author: para
"""
import matplotlib.pyplot as plt

def show_sequence(first,last,ts_x,ts_y,ts_e, delay=100, debug=False):
     """
     display sequence of time slices, from first to last, with delay in ms
     """
     name = '--->  show_sequence '
   
     plt.figure(figsize=(7,7)) 
       
     for ts in range(first,last):
        
        if debug:
            nhits = len(ts_e[ts])
            if nhits > 0:
                max_h = max(ts_e[ts])
            else:
                max_h = 0
                
            print name, '  time slice ',ts,'  nmber of hits = ', nhits, '  total energy ', sum(ts_e[ts]), ' max hit ',max_h

        plt.clf()
        plt.scatter(ts_x[ts],ts_y[ts],s=50*ts_e[ts])
        plt.title('zslice '+str(ts))
        plt.xlim([-250, 250])
        plt.ylim([-250, 250])
        plt.draw()
        plt.pause(0.001*delay)
     plt.show()