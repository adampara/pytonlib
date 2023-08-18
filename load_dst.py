#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:01:59 2019

@author: para
"""

import pandas as pd
import tables as tb

def load_dst(filename):
    """
    read dst file
    """
    
    with tb.open_file(filename) as h5:
        return pd.DataFrame.from_records(h5.root.DST.Events.read())