#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 09:33:05 2018

@author: para
"""

import numpy as np

def update_selection(i, ts_x, ts_y, ts_e, sel_x, sel_y, sel_e, classify,debug=False):
    """
    insert seleted hit into new selection and update cllasify flag
    """
    
    sel_x.append(ts_x[i])
    sel_y.append(ts_y[i])
    sel_e.append(ts_e[i])
    
    classify[i] = True
    
    
def cluster_sipm_info(ts_x, ts_y, ts_e, time_st, dist=15., debug=False):
    """
    separate the SiPM hits into clustered and isolated ones
    """

    name = '=== cluster_sipm_info  :'    
    sipm_wf_clust = np.zeros(len(time_st))
    sipm_wf_isol  = np.zeros(len(time_st))
    
    ts_x_clust = {}
    ts_y_clust = {}
    ts_e_clust = {} 
    
    ts_x_isol = {}
    ts_y_isol = {}
    ts_e_isol = {} 
  
    #   each hit can be custered or isolated 
    for tt in time_st:
        #   loop ove all time bins

        t = int(tt)
        if debug: print name, 'separate hits in time bin',t

        nhits = len(ts_x[t])        
        classif = [False]*nhits
        
        sel_x_clust = []
        sel_y_clust = []
        sel_e_clust = []
        
        sel_x_isol = []
        sel_y_isol = []
        sel_e_isol = []
          
        for i in range(nhits):
                      
            if debug: print name, 'classify hit number ',i, ts_x[t][i],ts_y[t][i]            
            if classif[i]: 
                if debug: print name,'  this hit has been classified already', i
                continue
            
            #  find adjacent hit in x
            for j in range(nhits):
                
                if i == j : continue

                if debug: print name, '           compare with hit number ',j, ts_x[t][j],ts_y[t][j]  
                if abs(ts_x[t][j] - ts_x[t][i]) < dist and abs(ts_y[t][j] - ts_y[t][i]) < dist:
                    #   success
                    if debug: print name, '   adjacent in x and y to the request hit'
                    update_selection(i, ts_x[t], ts_y[t], ts_e[t], sel_x_clust,sel_y_clust, sel_e_clust,classif)
                    if not classif[j]: update_selection(j, ts_x[t], ts_y[t], ts_e[t], sel_x_clust,sel_y_clust, sel_e_clust,classif)
                    if debug: print name,' done',i,j
                    break
                
            if classif[i]:
                if debug: print ' adjacent in x!'
                #  this hit has is adjacent in x
                continue
            else:
                if debug: print name, 'this hit is isolated'
                update_selection(i, ts_x[t], ts_y[t], ts_e[t], sel_x_isol,sel_y_isol, sel_e_isol,classif)

        if debug:                
            print name,'   initial hits , proximity distance ',dist      
            for i in range(nhits):
                print i, ts_x[t][i], ts_y[t][i], ts_e[t][i], classif[i]
            print name,'   clustered hits'
            for i in range(len(sel_x_clust)):
                print i, sel_x_clust[i],   sel_y_clust[i], sel_e_clust[i]           
            print name,'   isolated hits'
            for i in range(len(sel_x_isol)):
                print i, sel_x_isol[i],   sel_y_isol[i], sel_e_isol[i]   
                
        ts_x_clust[t] = np.asarray(sel_x_clust)
        ts_y_clust[t] = np.asarray(sel_y_clust)
        ts_e_clust[t] = np.asarray(sel_e_clust)
                        
        ts_x_isol[t] = np.asarray(sel_x_isol)
        ts_y_isol[t] = np.asarray(sel_y_isol)
        ts_e_isol[t] = np.asarray(sel_e_isol)

        sipm_wf_clust[t] = np.sum(ts_e_clust[t])
        sipm_wf_isol[t]  = np.sum(ts_e_isol[t])
        
    return sipm_wf_clust, ts_x_clust, ts_y_clust, ts_e_clust, sipm_wf_isol, ts_x_isol, ts_y_isol, ts_e_isol 