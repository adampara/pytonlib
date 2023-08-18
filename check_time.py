#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:10:07 2018

@author: para
"""
from __future__ import print_function

import time

def check_time(txt1,txt2):
    """
    print current time annotated with txt1 and txt2
    """
    
    print(txt1,txt2,time.process_time())