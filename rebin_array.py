#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:19:39 2018

@author: para
"""
from __future__ import division

from builtins import range
from past.utils import old_div
import numpy as np

def rebin_array(ar,n):
    """
    re-bin the array by a factor n into a numpy array
    """
    
    l_ar = len(ar)
    n_len = old_div(l_ar,n)
    if n_len*n < l_ar: n_len +=1
    

    
    reb_ar = np.zeros(n_len)
    
    for i in range(l_ar):
        n_ind = old_div(i,n)
        reb_ar[n_ind] += ar[i]
        
    return reb_ar       
        
    
    