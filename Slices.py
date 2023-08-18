# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:35:08 2017

@author: para
"""
from __future__ import print_function

from builtins import str
from builtins import object
import sys

from ROOT import gRandom, gPad, gROOT, gVirtualX, gSystem, TF1, gStyle
from ROOT import kTRUE, kRed
from ROOT import TCanvas, TH2, TH2F, Double


class DynamicExec(object):
   """Example of function called when a mouse event occurs in a pad.
When moving the mouse in the canvas, a second canvas shows the
projection along X of the bin corresponding to the Y position
of the mouse. The resulting histogram is fitted with a gaussian.
A "dynamic" line shows the current bin position in Y.
This more elaborated example can be used as a starting point
to develop more powerful interactive applications exploiting CINT
as a development engine.

Note that a class is used to hold on to the canvas that display
the selected slice.

Original author: Rene Brun
Modified and pythonized:  Johann Cohen-Tanugi, Wim Lavrijsen"""

   def __init__( self, Fit ):
      self._cX   = None
      self._cY   = None
      self._old  = None
      self.Fit   = Fit

   def __call__( self, Fit ):

      h = gPad.GetSelected();
      if not h:
         return

      if not isinstance( h, TH2 ):
         return

      gPad.GetCanvas().FeedbackMode( kTRUE )

    # erase old position and draw a line at current position
      px = gPad.GetEventX()
      py = gPad.GetEventY()

      uxmin, uxmax = gPad.GetUxmin(), gPad.GetUxmax()
      uymin, uymax = gPad.GetUymin(), gPad.GetUymax()
      pxmin, pxmax = gPad.XtoAbsPixel( uxmin ), gPad.XtoAbsPixel( uxmax )
      pymin, pymax = gPad.YtoAbsPixel( uymin ), gPad.YtoAbsPixel( uymax )

      if self._old != None:
         gVirtualX.DrawLine( pxmin, self._old[1], pxmax, self._old[1] )
         gVirtualX.DrawLine( self._old[0], pymin, self._old[0], pymax )
      gVirtualX.DrawLine( pxmin, py, pxmax, py )
      gVirtualX.DrawLine( px, pymin, px, pymax )

      self._old = px, py

      upx = gPad.AbsPixeltoX( px )
      x = gPad.PadtoX( upx )
      upy = gPad.AbsPixeltoY( py )
      y = gPad.PadtoY( upy )

      padsav = gPad

    # create or set the display canvases
      if not self._cX:
         print(h.GetName())
         self._cX = TCanvas( 'c2', h.GetName()+' Proj X', 730, 10, 700, 500 )
      else:
         self._DestroyPrimitive( 'X' )

      if not self._cY:
         self._cY = TCanvas( 'c3', h.GetName() + 'Proj Y', 10, 550, 700, 500 )
      else:
         self._DestroyPrimitive( 'Y' )

      self.DrawSlice( h, y, 'Y', x )
      self.DrawSlice( h, x, 'X', y )

      padsav.cd()

   def _DestroyPrimitive( self, xy ):
      proj = getattr( self, '_c'+xy ).GetPrimitive( 'Projection '+xy )
      if proj:
         proj.IsA().Destructor( proj )

   def DrawSlice( self, histo, value, xy, energy ):

      yx = xy == 'X' and 'Y' or 'X'

    # draw slice corresponding to mouse position
      canvas = getattr( self, '_c'+xy )
      canvas.SetGrid()
      canvas.cd()

      bin = getattr( histo, 'Get%saxis' % xy )().FindBin( value )
      hp = getattr( histo, 'Projection' + yx )( '', bin, bin )
      hp.SetFillColor( 38 )
      hp.SetName( 'Projection ' + xy )
      
      #   this is for fitting e-vs-z plots, revert to one of the opther options in general
      if xy == 'X':
          hp.SetTitle( 'Z val =  ' + str(round(value,2)) )     
      else:
          hp.SetTitle( 'Energy =  ' + str(round(value,2)) )  
      #hp.SetTitle( xy + 'Projection of bin=%d' % bin )
      #hp.SetTitle( xy + ' ' + str(round(value,2)) )      
      #if yx == 'Fit':     #  turned off fiting.. put X or Y to restore fits
      if yx == 'Y' and self.Fit :     #  turned off fiting.. put X or Y to restore fits  
         energy =          hp.GetBinCenter(hp.GetMaximumBin())
         hp.Fit( 'gaus', 'qrl', '', 0.9*energy, 1.1*energy )
         hp.GetBinCenter(hp.GetMaximumBin())
         hp.GetFunction( 'gaus' ).SetLineColor( kRed )
         hp.GetFunction( 'gaus' ).SetLineWidth( 2 )
         gStyle.SetOptFit(1)
      else:
         hp.Draw()
      canvas.Update()


#class DynamicExec_Proj():
#   """Example of function called when a mouse event occurs in a pad.
#When moving the mouse in the canvas, a second canvas shows the
#projection along X of the bin corresponding to the Y position
#of the mouse. The resulting histogram is fitted with a gaussian.
#A "dynamic" line shows the current bin position in Y.
#This more elaborated example can be used as a starting point
#to develop more powerful interactive applications exploiting CINT
#as a development engine.
#
#Note that a class is used to hold on to the canvas that display
#the selected slice.
#
#Original author: Rene Brun
#Modified and pythonized:  Johann Cohen-Tanugi, Wim Lavrijsen"""
#
#   def __init__( self ):
#      self._cX   = None
#      self._cY   = None
#      self._old  = None
#
#
#   def __call__( self ):
#
#      h = gPad.GetSelected();
#      if not h:
#         return
#
#      if not isinstance( h, TH2 ):
#         return
#
#      gPad.GetCanvas().FeedbackMode( kTRUE )
#
#    # erase old position and draw a line at current position
#      px = gPad.GetEventX()
#      py = gPad.GetEventY()
#
#      uxmin, uxmax = gPad.GetUxmin(), gPad.GetUxmax()
#      uymin, uymax = gPad.GetUymin(), gPad.GetUymax()
#      pxmin, pxmax = gPad.XtoAbsPixel( uxmin ), gPad.XtoAbsPixel( uxmax )
#      pymin, pymax = gPad.YtoAbsPixel( uymin ), gPad.YtoAbsPixel( uymax )
#
#      if self._old != None:
#         gVirtualX.DrawLine( pxmin, self._old[1], pxmax, self._old[1] )
#         gVirtualX.DrawLine( self._old[0], pymin, self._old[0], pymax )
#      gVirtualX.DrawLine( pxmin, py, pxmax, py )
#      gVirtualX.DrawLine( px, pymin, px, pymax )
#
#      self._old = px, py
#
#      upx = gPad.AbsPixeltoX( px )
#      x = gPad.PadtoX( upx )
#      upy = gPad.AbsPixeltoY( py )
#      y = gPad.PadtoY( upy )
#
#      padsav = gPad
#
#    # create or set the display canvases
#      if not self._cX:
#         self._cX = TCanvas( 'c2', 'Projection Canvas in X', 730, 10, 700, 500 )
#      else:
#         self._DestroyPrimitive( 'X' )
#
#      if not self._cY:
#         self._cY = TCanvas( 'c3', 'Projection Canvas in Y', 10, 550, 700, 500 )
#      else:
#         self._DestroyPrimitive( 'Y' )
#
#      self.DrawSlice( h, y, 'Y', x )
#      self.DrawSlice( h, x, 'X', y )
#
#      padsav.cd()
#
#   def _DestroyPrimitive( self, xy ):
#      proj = getattr( self, '_c'+xy ).GetPrimitive( 'Projection '+xy )
#      if proj:
#         proj.IsA().Destructor( proj )
#
#   def DrawSlice( self, histo, value, xy, energy ):
#
#      yx = xy == 'X' and 'Y' or 'X'
#
#    # draw slice corresponding to mouse position
#      canvas = getattr( self, '_c'+xy )
#      canvas.SetGrid()
#      canvas.cd()
#
#      bin = getattr( histo, 'Get%saxis' % xy )().FindBin( value )
#
#      hp = getattr( histo, 'Projection' + yx )( '', bin, bin )
#      hp.SetFillColor( 38 )
#      hp.SetName( 'Projection ' + xy )
#      hp.SetTitle( xy + 'Projection of bin=%d' % bin )
#      
#      if yx == 'noFit':  # this is to turn off fitting, put X or Y if Fit desired
#         hp.Fit( 'gaus', 'qrl', '', 0.6*energy, 1.4*energy )
#         hp.GetFunction( 'gaus' ).SetLineColor( kRed )
#         hp.GetFunction( 'gaus' ).SetLineWidth( 6 )
#      else:
#         hp.Draw()
#      canvas.Update()
#
#if __name__ == '__main__':
# # create a new canvas.
#   c1 = TCanvas('c1', 'Dynamic Slice Example', 10, 10, 700, 500 )
#   c1.SetFillColor( 42 )
#   c1.SetFrameFillColor( 33 )
#
# # create a 2-d histogram, fill and draw it
#   hpxpy  = TH2F( 'hpxpy', 'py vs px', 40, -4, 4, 40, -4, 4 )
#   hpxpy.SetStats( 0 )
#   x, y = Double( 0.1 ), Double( 0.101 )
#   for i in xrange( 50000 ):
#     gRandom.Rannor( x, y )
#     hpxpy.Fill( x, y )
#   hpxpy.Draw( 'COL' )
#
# # Add a TExec object to the canvas (explicit use of __main__ is for IPython)
#   import __main__
#   __main__.myslicer = DynamicExec()
#   c1.AddExec( 'dynamic', 'TPython::Exec( "myslicer()" );' )
#   c1.Update()
#gSystem.ProcessEvents()
##aa = input('aa')
