#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:33:36 2018

@author: para
"""
from __future__ import print_function

from builtins import zip
import numpy as np
from math import sqrt

def weighted_avg_and_std(values, weights, debug=False):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.

    """

    if debug: 
        name = '     =====   weighted_avg_and_std  '
        print(name, '  sum of weights  ', np.sum(weights))
        print(name, '   input arrays')
        for x,y in zip(values, weights):
            print(x,y)
            
    if np.sum(weights) > 0:
        average = np.average(values, weights=weights)
        variance = np.average((values-average)**2, weights=weights)
        std = sqrt(max(0.,variance))
    else:
        average = np.mean(values)
        std = 0.

    if debug: 

        print(name, '   weighted mean  ',average,'  sigma  ',std, '  variance  ',variance)

        
    return (average, std)        