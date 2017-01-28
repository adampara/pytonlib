# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 17:13:03 2016

@author: para
"""


def get_string(prompt):
    """
    get a string from a console
    """
    read = True
    while read:
        value = raw_input(prompt)
        if len(value) > 0:
            read = False
        else:
            print 'enter value'
    return value


def get_int(prompt):
    """
    get an integer from a console
    """
    read = True
    while read:
        value = raw_input(prompt)
        if len(value) > 0:
            try:
                valint = int(value)
                read = False
            except ValueError:
                print 'enter integer value'
                pass  # it was a string, not an int.

        else:
            print 'enter integer value'

    return valint


def get_float(prompt):
    """
    get a float from a console
    """
    read = True
    while read:
        value = raw_input(prompt)
        if len(value) > 0:
            try:
                valfloat = float(value)
                read = False
            except ValueError:
                print 'enter float value'
                pass  # it was a string, not a float.

        else:
            print 'enter a float value'

    return valfloat


def get_floats(prompt, nfloats):
    """
    get nfloats float from a console
    """
    read = True
    floats = []
    while read:
        value = raw_input(prompt)
        if len(value) > 0:
            tokens = value.split()
            if len(tokens) == nfloats:
                for i in range(nfloats):
                    try:
                        valfloat = float(tokens[i])
                        floats.append(valfloat)
                        if i == nfloats - 1:
                            read = False
                    except ValueError:
                        print 'enter float value'
                        pass  # it was a string, not a float.

        else:
            print 'enter ',nfloats, ' float value(s)'

    return floats

def get_ints(prompt, nints):
    """
    get nints integers from a console
    """
    read = True
    ints = []
    while read:
        value = raw_input(prompt)
        if len(value) > 0:
            tokens = value.split()
            if len(tokens) == nints:
                for i in range(nints):
                    try:
                        valint = int(tokens[i])
                        ints.append(valint)
                        if i == nints - 1:
                            read = False
                    except ValueError:
                        print 'enter integer  value'
                        pass  # it was a string, not an int.

        else:
            print 'enter ',nints, ' integer value(s)'

    return ints
