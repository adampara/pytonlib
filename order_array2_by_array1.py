#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:41:59 2020

@author: para
"""
from __future__ import print_function

from builtins import zip
import numpy                    as np
def order_array2_by_array1(ar1, ar2, debug=False):
    """
    

    Parameters
    ----------
    ar1 : iterable 
    ar2 : iterable
        

    Returns
    -------
    ar1_ord, ar2_ord  numpy array copies of the original arrays, 
    orderd by values of the ar1

    """
    

        
    aux = {}
    
    for a1, a2 in zip(ar1, ar2):
        aux[a1] = a2
        
    aa1 = []
    aa2 = []


    for a1 in np.sort(ar1):
        aa1.append(a1)
        aa2.append(aux[a1])
        
    if debug:
        print('  ---->   original arrays')
        print('first array   ',ar1)
        print(' second array ',ar2)
        print('  ---->  sorted arrays')
        print('first array   ',aa1)
        print(' second array ',aa2)
        
    return np.array(aa1), np.array(aa2)