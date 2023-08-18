#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:20:50 2023
vakyse of x in X, vaules of Yy in Y
calculate average of y in some range x1 and x2 and the values at the edges
@author: para
"""


import numpy as np

def get_avg_y_in_range(X, Y, X1, X2, num_points=100):
    
    # Generate a series of X values between X1 and X2
    interpolated_X = np.linspace(X1, X2, num_points)
    
    # Interpolate Y values for those X values
    interpolated_Y = np.interp(interpolated_X, X, Y)
    
    # Return the average of the interpolated Y values
    return np.mean(interpolated_Y), interpolated_Y[0], interpolated_Y[-1]