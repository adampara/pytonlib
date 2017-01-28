#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:03:29 2017

@author: para
"""

import os 
from int_input import get_int, get_ints
from ROOT import TCanvas, TH1F, TF1, TFile
import numpy as np


def sensitivity(lines):
    '''
    find the minimal distance between the elements in a list
    '''

    nlines = len(lines)
    lrec = 11
    nframe = nlines/lrec
    n_max = 10

    precision = 3   # precision of amplitude values
    sens = 10.

    for fr in range(min(n_max, nframe)):
        aa = lines[fr * lrec + 10].split()
        for j in range(1, len(aa)):
            dt = round(abs(float(aa[j]) - float(aa[j-1])), precision)
            if dt > 0 and dt < sens:
                sens = dt

    return sens


def select_file(datedir):
    """
    select a data file to analyze
    """
    
    datedirList = next(os.walk(datedir))[1]
    i = 0              
    for ddir in datedirList:
        print i,ddir
        i +=1
    
    idate = get_int('select date   ---> ')
    print 'anayze data taken on  ',datedirList[idate]
    
    seldatedir = datedir+datedirList[idate] + '/'
     
    # select temperature to analyze
    
    tempdirList = next(os.walk(seldatedir))[1]
    i = 0              
    for tdir in tempdirList:
        print i,tdir
        i +=1
    
    itemp = get_int('select temperature   ---> ')
    print 'analyze data taken at temperature',tempdirList[itemp]
    
    seltempdir = seldatedir + tempdirList[itemp] + '/'
    print seltempdir
    
    filel = next(os.walk(seltempdir))[2]
    fdat = []
    
    for f in filel:
        tok = f.split('_')
        if len(tok) < 2 or len(f)<5:
            continue
        if tok[1] != 'T' or f[-4:] == 'root':
            continue
        fdat.append(f)
    
    i = 0
    for f in fdat:
        print i, f
        i+=1
    
    ifile = get_int('select file   ---> ')
        
    print '  analyze file ',fdat[ifile]
    file = seltempdir + fdat[ifile]   
    print file
    return file
    
def parse(lines, sens):
    '''
    parse the data file, extract the waveforms and assign the absolute time
    sens is the least count of the amplitude values
    '''

    month = {'Jan': '01', 'Feb': '02', 'Mar': '03',
           'Apr': '04', 'May': '05', 'Jun': '06',
           'Jul': '07', 'Aug': '08', 'Sep': '09',
           'Oct': '10', 'Nov': '11', 'Dec': '12'}
    precision = 3   # precision of amplitude values

    wform = []
    acq_rec = []
    acq_no = -1
    tim = []
    ampl = []

    plot = False
    hist = False
    debug = False

    if hist:
        c = TCanvas("cv", "cv", 400, 300)
    f1 = TF1("f1", "gaus", -0.05, 0.05)
    h_val = TH1F('values', 'values', 101, -50 * sens, 50 * sens)

    nrec = 11       # number of lines in a frame record
    nskip = 1
    lskip = nrec * nskip    # number of lines to skip
    nlines = len(lines)
    #nlines = 5*nrec

    for j in range(lskip, nlines):

        i = j - lskip       # renumber the lines: process line j as if it was i
        lin_rec = i % nrec

        if i < 10:
            print i, '  ', lines[j]
        if i % nrec == 0:

            wf = lines[j].split()[1]    # waveform number

        if i % nrec == 1:
            acq = lines[j].split()[1]   # acquisition number

        if i % nrec == 2:
            dt = float(lines[j].split()[1])     # sampling frequency

        if i % nrec == 3:
            wlen = int(lines[j].split()[1])     # waveform length

        if i % nrec == 9:               # timestamp

            tok = lines[j][1:len(lines[j])-3].split()   # remove picoseconds
            tsa = (tok[2]+'-'+tok[0]+'-'+month[tok[1]]
                   )+'T'+tok[3]+tok[4]+tok[5]+'Z'       # convert to numpy
            tsb = np.datetime64(tsa)
            #  define the start of the frames, may discard some frames
            #  at the beginning to correct the data acquisition problems
            if i == 9:
                T0 = tsb        # first waveform
            tsc = tsb - T0      # time since the first waveform

            ts = int(str(tsc).split()[0])*1.e-9

        if i % nrec == 10:      # waveform data, last line of a record

            # waveform data
            aa = lines[j].split()
            values = []     # waveform value, floating point
            for k in range(len(aa)):
                values.append(round(float(aa[k]), precision))

            #  values is a waveform. Get the local baseline and subtract
            h_val.Reset()
            for i in range(len(aa)):
                h_val.Fill(values[i])
            h_val.Fit("f1", "RQ")
            mean = f1.GetParameter(1)   # baseline offest

            values_cor = []
            for i in range(len(values)):
                values_cor.append(values[i] - mean)

            if hist:
                c.cd()
                h_val.Draw()
                c.Update()

            for i in range(len(values_cor)):
                tt = ts + i*dt
                tim.append(tt)
                ampl.append(values_cor[i])

            if plot:
                plt.plot(aa)
                plt.show()

            entry = (wf, acq, ts)

            if acq_no != acq:
                #  new acquisition, if not the first one, store the previous
                if acq_no == -1:
                    acq_rec.append(entry)
                else:
                    wform.append(acq_rec)  # store the previous acquisition
                    acq_rec = []
                    acq_rec.append(entry)
                acq_no = acq
            else:
                acq_rec.append(entry)

            if j == len(lines)-1:
                wform.append(acq_rec)   # last line, store the last acquisition

    h_val.Delete()

    if debug:
        print 'length of the waveform = ',len(wform)
        print 'number of amplitude values ', len(ampl)
    del f1
    del h_val

    return wform, tim, ampl, dt, wlen

