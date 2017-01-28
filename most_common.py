# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:23:12 2017

@author: para
"""


def most_common(lst):
    """
    return the most common element in a list
    """
    return max(set(lst), key=lst.count)
