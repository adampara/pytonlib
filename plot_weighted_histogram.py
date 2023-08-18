#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:21:52 2023

@author: para

bin values of x weighted by y in nbins from xlow to xup
"""

import matplotlib.pyplot         as plt
import numpy                     as np

def plot_weighted_histogram(x, y, nbins, xlow, xup, plot=False, xl='Value', yl = 'Frequency', tit='Histogram'):

    # Calculate the bin edges
    bin_edges = np.linspace(xlow, xup, nbins + 1)

    # Compute the histogram values using weighted data
    hist_values, _ = np.histogram(x, bins=bin_edges, weights=y)

    # Plot the histogram
    plt.bar(bin_edges[:-1], hist_values, width=(xup - xlow) / nbins, edgecolor='black')
    
    #  annotate
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(tit)
    
    plt.grid(True)
    if plot: plt.show()
