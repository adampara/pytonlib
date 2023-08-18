#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:23:12 2020

@author: para
"""

import numpy                  as np 

def array_from_line(line, data_type='float'):
    """
    assume a line contains: keyword [list]
    extract list to a np array
    """

    first = line.find('[')
    last = line.find(']')

    string = line[first+1:last]
    ar = np.fromstring(string,dtype=data_type, sep=' ')    

    return ar