#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:16:49 2017
Organize files in a directory by years/months 
@author: para
"""

from os import listdir
from os.path import isfile, join
import datetime

direct = '/Users/para/ondrive/download/Photos/html/'
ext = 'html'
beg = 'day'
month = {
            '01': 'Jan',
            '02': 'Feb',
            '03': 'Mar',
            '04': 'Apr',
            '05': 'May',
            '06': 'Jun', 
            '07': 'Jul',
            '08': 'Aug',
            '09': 'Sep',
            '10': 'Oct',
            '11': 'Nov',
            '12': 'Dec'
            }


lfil = [f for f in listdir(direct) if isfile(join(direct, f))]
print lfil

fil_sel = []
dates = []
for f in lfil:
    print f, f[0:len(beg)], f[-len(ext):]
    if f[0:len(beg)] != beg or f[-len(ext):] != ext:
        continue
    fil_sel.append(f)
    tok = f.split('-')
    dates.append(f[4:15])

print dates    
ds = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%b-%d'))
print ds

oy = ''
file_name = direct + 'overview.html'
fn = open(file_name,'w')

fn.write( """<!doctype html>
<html>
<head>
<title>Our Funky HTML Page</title>
<meta name="description" content="Our first page">
<meta name="keywords" content="html tutorial template">
</head>
<body>""")

for d in ds:
    y = d[0:4]
    m = d[5:8]
    day = d[9:11]
    print y,m,day
    if y !=oy:
        oy = y
        print 'new year ', y
        fn.write('<h2> Year '+ y + '</h2>')
        om = ''
    if m != om:
        om = m
        print 'new month ',m
        fn.write('<h3>' + m + '</h3>')
    

        
    fn.write('<a href="file://' + direct + 'day_'+ y + '-' + m + '-' + day + '.html">' +  day + '</a>  ')
            
        