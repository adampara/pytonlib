#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:25:00 2017

@author: para
"""
from __future__ import print_function
from builtins import str
import pickle



def  in_str(lat,lng):
    """  
    header of the htmll file
    """

    in_str = """<!DOCTYPE html>
<html> 
<head> 
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
  <title>Google Maps Marker as a Link</title> 
  <script src="http://maps.google.com/maps/api/js?sensor=false" 
          type="text/javascript"></script>
</head> 
<body>
  <div id="map" style="width: 1400px; height: 1000px;"></div>

  <script type="text/javascript">
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: new google.maps.LatLng(""" + str(lat) + "," + str(lng) + """),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
"""
    
    return in_str

def marker_st(p,np):
    """
    marker block for every picture with GOS
    """
    lat = p[6]
    lng = p[7]
    
    m_str = """
            var marker""" + str(np)+ """ = new google.maps.Marker({
              position: {lat:""" + str(lat) +', lng:' + str(lng) + """},
              url: 'file://""" + p[0] + '/' + p[1] + """',
              icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 6
                   },
              map: map
              });
            
             google.maps.event.addListener(marker""" + str(np) + """, 'click', function() {
             window.open(marker""" + str(np) + """.url);
             });
    """
    
    return m_str

def end_st():
    """
    end of the file
    """
    
    end_str = """

</script>
</head>
<body>
  <div id="map_canvas"></div>
</body>
</html>
    """
    
    return end_str


def dat(day):
    """
    replace :mo: by -mon-
    """
    
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
    tok = day.split(':')
    nday = tok[0] + '-' + month[tok[1]] + '-' + tok[2]
    
    return nday
dir_file = '/Users/para/ondrive/download/Photos/directory_file'
pict = pickle.load(open(dir_file,"rb"))

for day in list(pict.keys()):
    print(day)

    if day != None:
#        if day != '2012:03:24':
#            print 'skip'
#            continue
        start = True
        np = 0
        for p in pict[day]:
            np += 1
            print(p)
            lat = p[6]
            lng = p[7]
            if p[6] != None and p[7] != None:
                
                if start:
                    #   first picture with GPS information trigger creation of the file
                    print('write a header, lat,lng', lat, lng)
                    route_file = '/Users/para/ondrive/download/Photos/html/day_' + dat(day) + '.html'
                    f = open(route_file,'w')
                    start = False  
                    init_str = in_str(lat,lng) 
                    f.write(init_str)
                    
                marker_string = marker_st(p,np)
                f.write(marker_string)    
                    

    if start:
        print('no geo information for day ',day)
    else:
        end_string = end_st()
        f.write(end_string)
        #f.close()