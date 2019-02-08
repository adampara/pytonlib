#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:26:03 2018

@author: para
"""

import numpy as np

def integrate_array(ar):
    """
    calculate an integrand of an array ar
    """
    
    br = np.zeros(len(ar))
    br[0] = ar[0]
    
    for ind in range(1,len(ar)):
        br[ind] = br[ind-1] + ar[ind]
       
    return br