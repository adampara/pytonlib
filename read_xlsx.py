#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:03:29 2017

@author: para
"""
from __future__ import print_function


def readXlsx( fileName, **args ):

    import zipfile
    from xml.etree.ElementTree import iterparse

    if "sheet" in args:
       sheet=args["sheet"]
    else:
       sheet=1
    if "header" in args:
       isHeader=args["header"]
    else:
       isHeader=False

    rows   = []
    row    = {}
    header = {}
    z      = zipfile.ZipFile( fileName )

    # Get shared strings
    strings = []
    strings = [ el.text for e, el
                        in  iterparse( z.open( 'xl/sharedStrings.xml' ) )
                        if el.tag.endswith( '}t' )
                        ]
    value = '' 

    # Open specified worksheet
    for e, el in iterparse( z.open( 'xl/worksheets/sheet%d.xml'%( sheet ) ) ):

       # get value or index to shared strings
       if el.tag.endswith( '}v' ):                                   # <v>84</v>
           value = el.text
       if el.tag.endswith( '}c' ):                                   # <c r="A3" t="s"><v>84</v></c>

           # If value is a shared string, use value as an index
           if el.attrib.get( 't' ) == 's':
               value = strings[int( value )]

           # split the row/col information so that the row leter(s) can be separate
           letter = el.attrib['r']                                   # AZ22
           while letter[-1].isdigit():
               letter = letter[:-1]

           # if it is the first row, then create a header hash for the names
           # that COULD be used
           if rows ==[]:
               header[letter]=value
           else:
               if value != '':

                   # if there is a header row, use the first row's names as the row hash index
                   if isHeader == True and letter in header:
                       row[header[letter]] = value
                   else:
                       row[letter] = value

           value = ''
       if el.tag.endswith('}row'):
           rows.append(row)
           row = {}
    z.close()
    return rows

if __name__ == "__main__":
    #print readXlsx( "/Users/para/Documents/SpaceX.xlsx")
    print(readXlsx( "/Users/para/DCR/S13360-3050CS.xlsx", sheet = 14, header = True))