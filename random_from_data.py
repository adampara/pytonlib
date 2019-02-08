#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:52:26 2018
return random numbers following the data distribution
@author: para
"""

import numpy as np
import scipy.interpolate as interpolate

def random_from_sample(data, n_bins, n_samples):
    
    hist, bin_edges = np.histogram(data, bins=n_bins, density=True)

    cum_values = np.zeros(bin_edges.shape)
    cum_values[1:] = np.cumsum(hist*np.diff(bin_edges))
    inv_cdf = interpolate.interp1d(cum_values, bin_edges,fill_value="extrapolate")
    print bin_edges,cum_values
    r = np.random.rand(n_samples)
    
    return inv_cdf(r)

def random_from_histogram(bin_edges,hist, n_samples):
    
    print type(hist)
    print type(bin_edges)
    cum_values = np.zeros(bin_edges.shape)
    cum_values[1:] = np.cumsum(hist)
    print bin_edges,cum_values
    inv_cdf = interpolate.interp1d(cum_values, bin_edges,fill_value="extrapolate")
    r = np.random.rand(n_samples)
    
    return inv_cdf(r)