#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:10:33 2018

@author: para
"""

def threshold_pos(arr, cut):
    """
    find the index of the array were the values cross the threshold
    """
    
    thr_pos = (arr > cut).argmax() if (arr > cut).any() else -1
    
    return thr_pos