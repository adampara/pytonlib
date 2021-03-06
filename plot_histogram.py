#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:50:11 2017

@author: para
"""


def plot_histogram(h,cvx=800,cvy=600,option='',file=''):
    """
    display histogram, dloblue click to close and continue the program flow
    """
    from ROOT import TCanvas,TImage
    
    c = TCanvas("cv", "cv", cvx, cvy)

    # c.cd()
    h.Draw(option)
    c.Update()

    if file != '':
        #   save histogram in a file
        img = TImage.Create()
        img.FromPad(c)
        img.WriteImage(file)
    #nto exit doubleclick on Canvas
    loop = True
    while loop:
        if c.WaitPrimitive() == None:
            loop = False
            c.Close()
            
    
