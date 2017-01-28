#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:31:51 2017
detecto if script is running from within Spyder environment
@author: para
"""

import os


def spyder():

    return any('SPYDER' in name for name in os.environ)
    
