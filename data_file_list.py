#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:05:27 2021

@author: para
"""

import os

def data_file_list(files,ffile,nfiles):
    """
    return a list of files to be analyzed

    """
    #   make list of files to analyze
    file_list = []
    
    found_file  = 0
    ifil        = 0
    
    max_part    = 20000    # upper limit on number of partitions 
    
    first_avail = -1
    last_avail  = 0
    while found_file < nfiles:

        file_num = ffile + ifil
        seq_num = format(file_num, '04d')
        fname = files.replace('XXXX',seq_num)
        
        #   check if file exists, add to the list of files
        if os.path.isfile(fname):
            file_list.append(fname)  
            found_file += 1
            
            if first_avail == -1: first_avail = int(seq_num)
            last_avail = int(seq_num)

        ifil += 1
        if ifil > max_part : break
    
    return file_list, first_avail, last_avail