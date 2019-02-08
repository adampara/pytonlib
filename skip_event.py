#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:19:01 2018

@author: para
"""

def skip_event(iev,nev_list):
    
    """
    skip event if nev_list not empty and iev si not in the list
    """

    if len(nev_list) == 0:
        skip = False
    else:
        if (iev in nev_list):
            skip = False
        else:
            skip = True
    
    return skip