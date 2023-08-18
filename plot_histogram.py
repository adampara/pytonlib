#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:50:11 2017

@author: para
Sun Apr 12 17:16:29 CDT 2020
   add optional zmin and zmax
Thu Jan  6 12:47:40 CST 2022
   add xmin, xmax in plot_histogram
"""
from __future__ import division
from __future__ import print_function

from past.utils import old_div
from ROOT import TCanvas,TImage,gSystem,TPaveText

def plot_histogram(h,cvx=800,cvy=600,option='',file='', zmin = -999., zmax = -999., 
                   xmin = -999., xmax=-999., stat='no', logy='N'):
    """
    display histogram, dooblue click to close and continue the program flow
    """
#    from ROOT import TCanvas,TImage
    
    c = TCanvas("cv", "cv", cvx, cvy)
    c.SetGrid()
    if logy == 'Y': c.SetLogy()
    if stat == 'no'  :   h.SetStats(0)
    
    if zmin != -999. and zmax != -999:
        h.SetMinimum(zmin)
        h.SetMaximum(zmax)
        
    if xmin != -999. and xmax != -999:
        h.GetXaxis().SetRangeUser(xmin, xmax)  
            
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
            gSystem.ProcessEvents()           
            del c

def plot_histogram_mojave(h,cvx=800,cvy=600,option='',file='', zmin = -999., zmax = -999., stat='no'):
    """
    display histogram, dooblue click to close and continue the program flow
    """
#    from ROOT import TCanvas,TImage
    
    c = TCanvas("cv", "cv", cvx, cvy)
    c.SetGrid()

    if stat == 'no'  :   h.SetStats(0)
    
    if zmin != -999. and zmax != -999:
        h.SetMinimum(zmin)
        h.SetMaximum(zmax)
        

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
            
            

import time

    
def pl_histogram_sequence(hlist, delay=0.5 ,cvx=800,cvy=600,option='', zmin = -999., zmax = -999.):
    """
    display histogram, dloblue click to close and continue the program flow
    """
#    from ROOT import TCanvas,TImage,gSystem
    
    c = TCanvas("cv", "cv", cvx, cvy)


    
    for h in hlist:
        time.sleep(delay) 
        h.SetStats(0)
        if zmin != -999. and zmax != -999:
            h.SetMinimum(zmin)
            h.SetMaximum(zmax)
        h.Draw(option)
        c.Modified()
        c.ForceUpdate()
        gSystem.ProcessEvents()
        c.Update()
   

    #nto exit doubleclick on Canvas
    loop = True
    while loop:
        if c.WaitPrimitive() == None:
            loop = False
            c.Close()
            
def pl_histogram_overlay(hlist_inp, cvx=800,cvy=600, option=' L ', zmin = -999., 
                         zmax = -999., n_max=7, stat='no', title='', 
                         file = '', logy = 'N', common_scale=False,
                         xmin = -999., xmax=-999., colors=[], mark_size=0.5):
    """
    overlay  histograms, double click to close and continue the program flow
    if less than nmax  histograms diferentiate colors and draw legend 
    colors may provide a list of colors for each histogram
    """
    from ROOT import  gPad

#  ---------  2021 March 24   ----- copy the histograms to a local list to allow for manipulaions not impacting the original histograms


    hlist = []
    
    for h in hlist_inp:
        hh = h.Clone()
        hlist.append(hh)
        

#  -------   normalize all histograms to the same peak values
    if common_scale:
        
        min_val = 1.e10
        max_val = -min_val
 
        for h in hlist:                
            max_val = max(max_val,h.GetMaximum())  
            
        for h in hlist:                
            max_v = h.GetMaximum()   
            h.Scale(old_div(max_val,max_v))
#    --------------------------------------
        
    c = TCanvas("cv", "cv", cvx, cvy)
    c.SetGrid()
    tpavetext = TPaveText(0.1,0.9,0.9,1.,"brNDC")
    if logy == 'Y': c.SetLogy()
    n_hist = len(hlist)           

    item = 0


        
#   --------  2021, Jan 23  --- normalize to common range if range not given

    print(('zmin, zmax', zmin, zmax))
    if zmin == -999.0 and zmax == -999.0:
        
        print ('   normalise histograms')
        
        min_val = 1.e10
        max_val = -min_val
 
        for h in hlist:

            eps = 1.e-5
            if logy=='Y': 
                min_val = min(min_val,h.GetMinimum(eps))
            else:
                min_val = min(min_val,h.GetMinimum())
                
            max_val = max(max_val,h.GetMaximum())  
 
        marg = 0.5    #   (how much margin beyond the true range())   
          
        if min_val > 0:
            min_val = (1.- marg) * min_val
        else:
            min_val = (1.+ marg) * min_val

        if max_val > 0:
            max_val = (1. + marg) * max_val
        else:
            max_val = (1.- marg) * max_val

        print(('   forced range  ',min_val, max_val))                        
        for h in hlist:
                h.SetMinimum(min_val)
                h.SetMaximum(max_val)
                
                
#    --------------------------------   end of normalization     

    ncol = 5
    #option += ' p '   
    for h in hlist:

        if stat == 'no'  :   h.SetStats(0)

        h.SetLineWidth(3)        
        if n_hist < n_max:   
            if len(colors)==0:        # set colors automatically
                h.SetLineColor((item+1)%ncol+1)
            else:                      # assign color externally
                h.SetLineColor(colors[item])
            
        if zmin != -999. and zmax != -999:
            h.SetMinimum(zmin)
            h.SetMaximum(zmax)

        if xmin != -999. and xmax != -999:
            h.GetXaxis().SetRangeUser(xmin, xmax)  
            
        h.SetMarkerStyle(20+item)
        h.SetMarkerSize(mark_size)
        if len(colors)==0:        # set colors automatically
            h.SetMarkerColor((item+1)%ncol+1)
        else:                      # assign color externally
            h.SetMarkerColor(colors[item])

        
        if item == 0:               # first histogram to 
            #print ('  first to draw', h.GetTitle(),h.GetMinimum(), h.GetMaximum(), option)
            h.Draw(option) 

        else:
            #print ('  second to draw', h.GetTitle(),h.GetMinimum(), h.GetMaximum(), option)
            h.Draw(' SAME ' + option)

        c.Update()
           
        item += 1
    
    if n_hist < n_max   :   gPad.BuildLegend()
    tpavetext.AddText(title)
    tpavetext.Draw()
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
            