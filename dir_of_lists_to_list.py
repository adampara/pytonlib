#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:54:16 2021
convert a dictionary of lists into a list

@author: para
"""

def dir_of_lists_to_list(dictionary):
    
    """ 
    convert a dictionary of lists into a global list
    For example to pass to Save_Hist
    """
    
    gl_list = []
    
    for k in dictionary:
        
        obj = dictionary[k]
    
        if isinstance(obj, list):
            
            for l_el in obj:
                gl_list.append(l_el)
        else:
                
            print("item is not a list", type(obj))
            exit()
            
    return gl_list