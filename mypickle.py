#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:26:52 2019

@author: para
"""

import pickle                  as pl

def my_pickle_dump(struct, filenam):
    """
    store pickled structure
    """

    fo = open(filenam, "wb")
    str_ser = pl.dumps(struct)
    fo.write( str_ser)
    fo.close()
    
    
def my_pickle_load(filenam):
    """
    load pickled structure
    """    

    fo = open(filenam, "rb")
    str_ser = fo.read( )
    struct = pl.loads(str_ser)
    fo.close()

    return struct