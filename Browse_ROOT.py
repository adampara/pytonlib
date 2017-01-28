# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:13:51 2017

@author: para
"""

from ROOT import TBrowser, gSystem


def Browse_ROOT():
    """
    open TBrowser and allow for inspection of ROOT histograms
    """

    t = TBrowser()
    #  to exit select 'interrupt' in Options
    loop = True
    while loop:
        gs = gSystem.ProcessEvents()
        if gs:
            break
        else:
            continue
    t.Delete()
