#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 12:07:08 2018

@author: para
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:53:59 2018

@author: para
"""

def histogram_mean(hist):
    """
    histogram mean value and its error
    """

    mean = hist.GetMean()
    mean_err = hist.GetMeanError()
    
    return mean, mean_err


