#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:50:11 2017

@author: para
"""


def overlay_histograms(hl,cvx=800,cvy=600,option='',op = ''):
    """
    display ovrelayed histograms, doblue click to close and continue the program flow
    """
    from ROOT import TCanvas
    
    c = TCanvas("cv", "cv", cvx, cvy)

    # c.cd()
    if op == 'add' :
        i = 0
        for h in hl:
            i += 1
            if i == 1:
                h.SetMinimum(1.e-4)
                hs = h.Clone()

            else:
                hs.Add(h)
                h.Draw('same'+option)
        hs.Draw(option)
        c.Update()
    else:
        i = 0
        for h in hl:
            i += 1
            if i == 1:
                h.SetMinimum(1.e-4)
                h.Draw(option)
                c.Update()
            else:
                h.Draw('same'+option)
                c.Update()

    #nto exit doubleclick on Canvas
    loop = True
    while loop:
        if c.WaitPrimitive() == None:
            loop = False
            c.Close()
            
    return hs

