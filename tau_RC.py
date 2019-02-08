#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:27:26 2018

@author: para
"""

def tau_RC():
    """
    define RC constants for all PMTs
    values are vro the exponential fits
    
    """
    
    
    tau = { 0  :  0.000528448223727 ,
            1  :  0.000534286124735 ,
            2  :  0.000531127097197 ,
            3  :  0.000528590936727 ,
            4  :  0.000523307118588 ,
            5  :  0.000531484578773 ,
            6  :  0.000522540813269 ,
            7  :  0.000529130885772 ,
            8  :  0.000527471895065 ,
            9  :  0.000527267947332 ,
            10 :  0.000529931735586 ,
            11 :  0.000527613470536 }
    
    return tau