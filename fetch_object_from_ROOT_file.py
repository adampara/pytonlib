#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:12:30 2019

@author: para
"""
from __future__ import print_function

from ROOT                import TFile, gDirectory

def fetch_object_from_ROOT_file(fname,obj):
    
    f = TFile(fname)

    fobj = f.Get(obj)

    if (gDirectory.FindObject(obj)):

        fobj.SetDirectory(0)
    else:
        print('Object ', obj, ' does not exis in file', fname) 
        fobj = None
         
    return fobj