#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:52:41 2019

@author: para
"""
from __future__ import print_function

import datetime
import numpy                  as np
from load_dst                 import load_dst
     

def beg_end_run(d_dir, run, files):
    """
    determine begin/end of the run in a given data set (files)
    """
    
    
    print('-----------  Run time Time    ---------')
    
    
    t_zone_off = 7*3600
    
    data_dir = d_dir + '/' + run + '/'
    
    full = load_dst(data_dir+files[0])
    evno = np.asarray(full['event'])  
    time = np.asarray(full['time'])    
    t_beg = time[0]
    first_ev_number = evno[0]
    date_beg = datetime.datetime.fromtimestamp(t_beg+t_zone_off)   
    
    full = load_dst(data_dir+files[-1])
    evno = np.asarray(full['event'])  
    time = np.asarray(full['time']) 
    last_ev_number = evno[-1]
    t_end = time[-1]
    date_end = datetime.datetime.fromtimestamp(t_end+t_zone_off)    
    
    
    print('   First data file  ',files[0])
    print('   Last data files  ',files[-1])
    
    print('')
    #    timestamps are in Canfranc time zone, datatime is using the local time zone
    print('first event  number       ', first_ev_number, '   timestamp  ',t_beg, date_beg)
    print('last  event  number ',  last_ev_number, '   timestamp  ',t_end, date_end)
    
    return (t_beg, date_beg, first_ev_number, t_end, date_end, last_ev_number)