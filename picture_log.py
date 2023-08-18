#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:25:00 2017
print a log of addresses for each day
@author: para
"""
from __future__ import print_function
import pickle
import unicodedata



dir_file = '/Users/para/ondrive/download/Photos/directory_file'
pict = pickle.load(open(dir_file,"rb"))

for day in list(pict.keys()):
    print(day)

    if day != None:
#        if day != '2012:03:24':
#            print 'skip'
#            continue
        start = True
        
        loc = 'unknown'
#        #experiment with adresses
#        for p in pict[day]:
#            print p
#            (path, filename, date, camera, length, width, lat, lon, address) = p
#            if address == None:
#                continue
#            
#            tok = address.split(',')
#            print len(tok), tok
#            
#
#         exit()
         
        for p in pict[day]:
            print(p)

            if start:
                #   first picture trigger creation of the file

                route_file = '/Users/para/ondrive/download/Photos/log/day_' + day + '.log'
                print('write a header, log file = ',route_file)
                f = open(route_file,'w')
                f.write( """<!doctype html>
<html>
<head>
<title>Our Funky HTML Page</title>
<meta name="description" content="Our first page">
<meta name="keywords" content="html tutorial template">
</head>
<body>
<h2> Date """ + day + '</h2>')
                start = False  
                
            (path, filename, date, camera, length, width, lat, lon, address) = p
            if address == None:
                address = u'unknown'
            marker_string = 'diretory ' + path + ' file ' + filename + ' date ' + date + ' location ' + unicodedata.normalize('NFKD', address).encode('ascii','ignore') + '\n'
            location =  unicodedata.normalize('NFKD', address).encode('ascii','ignore')
            if location == loc and loc != 'unknown' :
                loc_str = ''    # the same location, print nothing
            else:
                #   truncate the location
                loc_str = location
                loc = location
            marker_string = '<p><a href = file://' + p[0] + '/' + p[1] + '>' + date.split()[1] + '</a>'  + loc_str + '\n</p>'
            f.write(marker_string)   
            
                

    if start:
        print('no geo information for day ',day)
