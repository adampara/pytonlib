#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:19:16 2017
print address, disable pickle (Oct 5,2017)
@author: para
"""
import os
from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from geopy.geocoders import Nominatim
import pickle
import exifread
import time
from transliterate import translit
import unicodedata
import goslate

# based on https://gist.github.com/erans/983821

def _get_if_exist(data, key):
    if key in data and len(data[key].values)>0  :
        return data[key]

    return None


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)
    
def get_exif_location(exif_data):
    """
    Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
    """
    lat = None
    lon = None

    gps_latitude = _get_if_exist(exif_data, 'GPS GPSLatitude')
    gps_latitude_ref = _get_if_exist(exif_data, 'GPS GPSLatitudeRef')
    gps_longitude = _get_if_exist(exif_data, 'GPS GPSLongitude')
    gps_longitude_ref = _get_if_exist(exif_data, 'GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = 0 - lon

    return lat, lon

stop_tag = DEFAULT_STOP_TAG
debug = False
strict = False
color = False
detailed = True
logger = exif_log.get_logger()
geolocator = Nominatim()

numb = 0

#pict = {}    # Oct 6 2017   make the directory local to a directory file

for path, subdirs, files in os.walk('/Users/para/ondrive/download/Photos_old/'):
   print ' analyze ',path
   pict = {}
   dir_file = path + '/directory_file'
   if os.path.isfile(dir_file):
       continue
   for filename in files:
     f = os.path.join(path, filename)
     numb += 1
     if filename[0:5] == 'thumb':
         continue
     if filename[-3:] == 'JPG' or filename[-3:] == 'jpg' :

         img_file = open(str(f), 'rb')
         data = process_file(img_file, stop_tag=stop_tag, details=detailed, strict=strict, debug=debug)
    

         lat, lon = get_exif_location(data)
         address = None
         
         if lat and lon:
             print filename, lat,lon
             rev = str(lat) + ', ' + str(lon)
             try:
                 location = geolocator.reverse(rev,language='en')
                 address = location.address
#                 addr_ru = translit(addr, 'ru' ,reversed=True)
#                 addre = unicodedata.normalize('NFKD', addr_ru).encode('ascii','ignore')
#                 gs = goslate.Goslate()
#                 address = gs.translate(addre,'en')

                 print address
             except:
                 address = None
                 print ' did not get an adddress for location',rev
                     
             time.sleep(1.)
#         for i in data.keys():
#             print i
         if 'EXIF DateTimeOriginal' in data.keys():
             date =  data['EXIF DateTimeOriginal'].values + ' ' + str(numb)
             day = date.split()[0]
         else:
             date = None
             day = None
         #print day
         if 'EXIF ExifImageLength' in data.keys():
             length = data['EXIF ExifImageLength'].values[0]
         else:
             length = None
         if 'EXIF ExifImageWidth' in data.keys():
             width =  data['EXIF ExifImageWidth'].values[0]
         else:
             width = None
    
         if 'Image Model' in data.keys():
             camera =  data['Image Model'].values
         else:
             camera = None
         
         #print path, filename, date, camera, length, width, lat, lon, address
         
         if day not in pict.keys():
             print 'new  day ', day
             pict[day] = []
            
         pict[day].append((path, filename, date, camera, length, width, lat, lon, address))
   
   pickle.dump(pict, open(dir_file,"wb"))  
   
#    Oct 6, 2017   diretories written to local files
   
#for day in pict.keys():
#     print day
#     
#dir_file = '/Users/para/ondrive/download/Photos/directory_file'
#pickle.dump(pict, open(dir_file,"wb"))