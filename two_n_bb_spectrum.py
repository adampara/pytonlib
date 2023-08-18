#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:38:53 2020

@author: para
"""
from __future__ import division

from past.utils import old_div
def two_n_bb_spectrum(K,Qbb):
    """
    two neutrino decay summed electron spectrum

    Parameters
    ----------
    K   : summed electron energy, in electron mass units
    Qbb : in electron mass units


    Returns
    -------
    P :Relative probability

    """
    
    T0 = Qbb 
    
    if K < T0:
        
        P = K * (T0 - K)**5 * (1 + 2*K + 4.*K**2/3. + old_div(K**3,3) + K**4/30. ) 
        
    else:
        P=0.

    
    return P

