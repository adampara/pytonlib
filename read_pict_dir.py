#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:25:00 2017

@author: para
"""
import pickle



def  in_str(lat,lng):
    """  
    header of the htmll file
    """

    in_str = """<!DOCTYPE html> 
<html> 
<head> 
<title>Draw a daily route</title> 

<meta name="viewport" content="initial-scale=1.0, user-scalable=no" /> 
<style type="text/css"> 
html { height: 100% }
body { height: 100%; margin: 0; padding: 0 } 
#map_canvas { height: 100% } 
</style> 
<script type="text/javascript" src="http://maps.googleapis.com/maps/api/js"></script> 

<script> 
    function initialize() { 
        var homeLatlng = new google.maps.LatLng(""" + str(lat) + ',' + str(lng) + """); 
        var myOptions = { 
            zoom: 5, 
            center: homeLatlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
        """
    return in_str

def marker_st(len,lng):
    """
    marker block for every picture with GOS
    """
    
    m_str = """
            var marker = new google.maps.Marker({
          //position: map.getCenter(),
          position: {lat:""" + str(lat) +', lng:' + str(lng) + """},
          icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 6
          },
          map: map
        });
    """
    
    return m_str

def end_st():
    """
    end of the file
    """
    
    end_str = """
        }

    google.maps.event.addDomListener(window, 'load', initialize);
</script>
</head>
<body>
  <div id="map_canvas"></div>
</body>
</html>
    """
    
    return end_str

dir_file = '/Users/para/ondrive/download/Photos/directory_file'
pict = pickle.load(open(dir_file,"rb"))

for day in pict.keys():
    print day

    if day != None:
#        if day != '2012:03:24':
#            print 'skip'
#            continue
        start = True
        
        for p in pict[day]:
            print p
            lat = p[6]
            lng = p[7]
            if p[6] != None and p[7] != None:
                
                if start:
                    #   first picture with GPS information trigger creation of the file
                    print 'write a header, lat,lng', lat, lng
                    route_file = '/Users/para/ondrive/download/Photos/html/day_' + day + '.html'
                    f = open(route_file,'w')
                    start = False  
                    init_str = in_str(lat,lng) 
                    f.write(init_str)
                    
                marker_string = marker_st(lat,lng)
                f.write(marker_string)    
                    

    if start:
        print 'no geo information for day ',day
    else:
        end_string = end_st()
        f.write(end_string)
        #f.close()