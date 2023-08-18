#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:27:26 2018
Updated on Fri Dec 17 14:46:45 CST 2021

alpha events used with exponential fit over the whole range for several low background runs
add run num,ber as an argument, use old values as a default

@author: para
"""

def tau_RC(run = 0):
    """
    define RC constants for all PMTs
    values are from the exponential fits
    
    """


    tau = {}
    
    tau[0] = { 0  :  0.000528448223727 ,
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
    
        
    tau[8088] = { 0  :  5.31332e-04  ,
                  1  :  5.36915e-04  ,
                  2  :  5.32637e-04 ,
                  3  :  5.30414e-04    ,
                  4  :  5.32376e-04 ,
                  5  :  5.42936e-04  ,
                  6  :  5.30456e-04 ,
                  7  :  5.39265e-04 ,
                  8  :  5.29270e-04 ,
                  9  :  0.000529219 ,
                  10 :  5.29847e-04 ,
                  11 :  5.28952e-04  }
        
    tau[8089] = { 0  :  5.31416e-04 ,
                  1  :  5.37008e-04  ,
                  2  :  5.33042e-04 ,
                  3  :   0.000530479 ,
                  4  :   5.32518e-04  ,
                  5  :   5.42983e-04 ,
                  6  :   5.30310e-04 ,
                  7  :   5.39168e-04 ,
                  8  :   0.000529401 ,
                  9  :   0.000529229 ,
                  10 :   0.000530108  , 
                  11 :   0.000529216 }
    
        
    tau[8678] = { 0  :  5.31343e-04 ,
                  1  :  5.36915e-04  ,
                  2  :  5.32922e-04  ,
                  3  :  0.000530248  ,
                  4  :  0.000532365 ,
                  5  :  0.000542388 ,
                  6  :  0.000530768 ,
                  7  :  0.000539662 ,
                  8  :  0.000529246 ,
                  9  :  0.00052921 ,
                  10 :  0.000529816 ,
                  11 :  0.000529137 }

    if run not in tau:
        print ('   tau_RC, requested run ', run , ' not available, default used')
        run = 0  
        
    return tau[run]