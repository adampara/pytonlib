
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:52:36 2019
convert 2d x-y histogram to a 1-D radial histogram 
@author: para
"""

from builtins import range
from ROOT                   import TH1F
import math 
def convert_xy_to_radial(H2D,title,n_rad_bin, rad_max):
    """
    calculat radial distribution from x-y map
    """
        
    nbinx = H2D.GetNbinsX()
    nbiny = H2D.GetNbinsY()
    
    h_rad = TH1F(title,title, n_rad_bin, 0., rad_max)
        
    for ix in range(nbinx):
        for iy in range(nbiny):
            val = H2D.GetBinContent(ix+1,iy+1)
            xval = H2D.GetXaxis().GetBinCenter(ix+1)
            yval = H2D.GetYaxis().GetBinCenter(iy+1)    
            
            rad = math.sqrt(xval**2 + yval**2)
            h_rad.Fill(rad, val)
            
    return h_rad