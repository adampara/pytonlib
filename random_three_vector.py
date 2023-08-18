#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 05:24:26 2018

@author: para
"""
from builtins import range
import numpy as np

def random_three_vector(N):
    """
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    threetups = []
    
    for i in range(N):
        phi = np.random.uniform(0,np.pi*2)
        costheta = np.random.uniform(-1,1)
    
        theta = np.arccos( costheta )
        x = np.sin( theta) * np.cos( phi )
        y = np.sin( theta) * np.sin( phi )
        z = np.cos( theta )
        threetups.append((x,y,z))
    return threetups

