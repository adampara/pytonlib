#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:57:32 2017
root utilities
@author: para

Mon Jan  6 11:43:57 CST 2020
removed gDirectory.pwd() lines  (commented for now)
"""
from __future__ import print_function
from builtins import range
from ROOT import gRandom, TCanvas, TH1F, TFile, TTree,TH2F,gDirectory, TF1,TF2,gStyle


def GetKeyNames ( self) :
    return [name.GetName() for name in self.GetListofKeys()]

TFile.GetKeyNames = GetKeyNames

def ldir(dirname,MyFile, Sel_Dir='',debug=False):
    """
    return list af all histgrams in a root file
    """
    
    hh= []      # list of histograms

    savdir = gDirectory.GetPathStatic()
    savd = gDirectory
    if debug:
        print('   initial directory  ', savd, '        ', savdir)
    
    lk1 = dirname.GetListOfKeys()    

    for key in lk1:

        if debug:
            print('  =======  Key found  ',key.GetName(),key.GetClassName())
        if(key.GetClassName() == 'TH1F' 
           or key.GetClassName() == 'TH2F' 
           or key.GetClassName() == 'TH3F' 
           or key.GetClassName() == 'TProfile' 
           or key.GetClassName() == 'TProfile3D' 
           or key.GetClassName() == 'TProfile2D'):
            #  check if this directory is selected
            if len(Sel_Dir) < 1 or (
                len(Sel_Dir)>1 and savdir.split('/')[-1] == Sel_Dir):
                hh.append(key)

                # below is an example of accessing a tree.
        if  key.GetClassName() == 'TTree':
             tree = MyFile.Get(key.GetName())             
             branches =  tree.GetListOfBranches()
             
             if debug:
                 print('    Class = ', key.GetClassName())
                 print('   --- tree    ---\n',tree)


                 print('  ----branches----- \n',branches)
                 print(branches.GetEntries())

             for i in range(0,branches.GetEntries()):
                 branch = branches.At(i)
                 print(branch)
                 print(branch.GetName())

             leaves = tree.GetListOfLeaves()
             print('  leaves list of entries')
             print(leaves)
             print(leaves.GetEntries())

             for i in range(0,leaves.GetEntries()):
                 leaf = leaves.At(i)
                 print(leaf)
                 print(leaf.GetName())
                 #    GetLen is the number of elements
                 #    it is 0 if it is specified in another leaf
                 print(leaf.GetLen())

             tree.GetEntry(15)
             print(' Number of waveform points ')
             print(leaves.At(0).GetValue())
             np = int(leaves.At(0).GetValue())
             print(np)
             for i in range (0,np):
                 print(i, leaves.At(1).GetValue(i))


        if  key.GetClassName() == 'TDirectoryFile':

            dirname.cd(key.GetName())
            
            if debug:
                print('This key is a directory,', key.GetName())
                print(' Current directory is ')
            #gDirectory.pwd()

            dirn = gDirectory
            hh.extend(ldir(dirn,MyFile,Sel_Dir=Sel_Dir))

            gDirectory.cd('..')
            #gDirectory.pwd()

            savd.cd()
            #gDirectory.pwd()
            if debug:
                print(savdir)
            gDirectory.cd(savdir)
            #Directory.pwd()

            continue

            if debug:
                print('   after the loop, savdir ' ,savdir)
                print('   after the loop, savd ' ,savd)
                print('     end of a listing of a directory  ')

    return hh
