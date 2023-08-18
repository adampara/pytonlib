#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:05:54 2023

@author: para
"""


def sort_y_based_on_x(x, y):
    # Combine x and y arrays into pairs
    pairs = list(zip(x, y))

    # Sort the pairs based on the values of x in ascending order
    sorted_pairs = sorted(pairs, key=lambda pair: pair[0])

    # Extract the sorted y values
    sorted_y = [pair[1] for pair in sorted_pairs]

    return sorted_y
