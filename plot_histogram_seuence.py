#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Created Mon Jul  6 14:33:29 CDT 2020
@author: para


pot a timed sequence of histograms 
"""

import time

    
def pl_histogram_sequence(hlist, delay=1. ,cvx=800,cvy=600,option='', zmin = -999., zmax = -999.):
    """
    display histogram, dloblue click to close and continue the program flow
    """
    from ROOT import TCanvas,TImage
    
    c = TCanvas("cv", "cv", cvx, cvy)

    for h in hlist:

        if zmin != -999. and zmax != -999:
            h.SetMinimum(zmin)
            h.SetMaximum(zmax)
        h.Draw(option)
        c.Update()
        time.sleep(delay)


    
