#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:19:16 2017
print address, disable pickle (Oct 5,2017)
@author: para
"""
from __future__ import print_function
from builtins import str
import os
from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from geopy.geocoders import Nominatim
import pickle
import exifread
import time
from geopy.geocoders import Nominatim
import unicodedata
from transliterate import translit
from translate import Translator
from datetime import datetime
from pytz import timezone
import goslate
from langdetect import detect
#from polyglot.detect import Detector

def local(lat,lon,time):
    from tzwhere import tzwhere
    geolocator = Nominatim()
    tzwhere = tzwhere.tzwhere()
    address = None
     

    
    print(lat,lon)
    rev = str(lat) + ', ' + str(lon)
    
    location = geolocator.reverse(rev,language='en')
    address = location.address
     
             
    print(address)
    #print languages()
    #print Detector(address)
    exit()
    #print 'languege  ',detect(address)
    ad_str = unicodedata.normalize('NFKD', address).encode('ascii','ignore')
    print(translit(address, 'ru' ,reversed=True))
    print(ad_str)
    translator= Translator(to_lang="en")
    #translator= Translator(from_lang="zh")
    tr = translator.translate(address)
    print(tr)
#    gs = goslate.Goslate()
#    print gs.translate(address,'en')
    timezone_str = tzwhere.tzNameAt(lat,lon)
    print(timezone_str)
    
    dat = "2009-05-05 22:28:15"
    datetime_obj = datetime.strptime(dat, "%Y-%m-%d %H:%M:%S")
    datetime_Chicago = datetime_obj.strptime(dat, "%Y-%m-%d %H:%M:%S")
    print(datetime_Chicago)    
    dt = datetime_obj.replace(tzinfo=timezone('US/Central'))
    datetime_there = dt.astimezone(timezone(timezone_str))
    print('==========. ',datetime_there)
    timez = timezone(timezone_str)
    dt = datetime.now()    
    print(timez.utcoffset(dt))
    
    date_str = "2014-05-28 22:28:15"
    datetime_obj_naive = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    # Right way!
    datetime_obj_pacific = timezone('US/Pacific').localize(datetime_obj_naive)
    print(datetime_obj_pacific.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    
    date_str = "2009-05-05 22:28:15"
    datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('US/Central'))
    print(datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    print(now_utc.strftime(fmt))
    
    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    print(now_pacific.strftime(fmt))
    
    # Convert to Europe/Berlin time zone
    now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
    print(now_berlin.strftime(fmt))
    
if __name__ == '__main__':
    
        tim = '01:16:28'
        lat, lon = ( 35.7898383333, 129.331518333)
        local(lat,lon,tim) 
        lat, lon = (39.8918766667, 116.315833333)
        local(lat,lon,tim)
        exit()
        lat, lon = (59.9365916667,30.3016383333)
        tim = '01:16:28'
        local(lat,lon,tim)
        lat,lon = (29.288719444444446, 90.90053333333334)
        local(lat,lon,tim)