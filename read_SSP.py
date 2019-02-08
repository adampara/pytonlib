# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:30:43 2017

@author: para
"""

from bitstring import BitArray
import numpy as np

def read_SSP(dfile, hex=True, maxev = 999999999, deb=-1, get_header=False):
    """
    Read the data file with SSP information
    Nov 7 2018   recoginze the hex/dec files by header, keep 'hex' forbackward compatibility
    """
    debug_level = 2
    debug = False
    marker_dec = '43690'
    marker_hex = 'AAAA'
    marker = 43690
    
    if  debug_level < deb: debug = True

 
    
    f = open(dfile)

    evno = 0
        
    hex = 'test'        #   special value to use the first line to figure out hex/decimal
    line_number = 0
    
    data_lines =  f.read().splitlines()
    if debug:
        print 'data file length = ', len(data_lines)
        
    lines_to_read = min(len(data_lines),2024*(maxev+1))
    lines = np.empty(lines_to_read)    #   array to hold the inut file lines
    
    for i in range(lines_to_read):      # parse the input lines into header and waveform

        line = data_lines[i]
        line_number += 1
          
        if len(line)>0:
            if hex == 'test':
                if line == marker_hex:
                    hex = True
                    
                if line == marker_dec:
                    hex = False
                if hex == 'test':
                    print 'incorrect header, cannot determine file encoding  ',line
                    exit()
            if hex:
                ln = int(line,16)
            else:
                if line.isdigit():      # protect agains I/O error, take previous number
                    ln = int(line)  
                else:
                    print 'bad line ',line_number, '  data  ',line, '  replaced by ',lines[i-1] 
                    ln = lines[i-1]    #  take the previous line as the best giess to replace the incorrect value

            lines[i] = ln    #  assume the the previous line was a valid number, if the current one is not
    
    nlines = len(lines)
    
    if debug:
        print 'read_SSP: read file ',dfile,'  Number of lines = ',len(lines)    

    nhead = 24      # length of header (in16 bit words)
    nsh = 2**16     # factor to shift by 16 bits

    pointer = 0     # pointer to the beginning of a current waveform
    loop = True     # control of the loop over the desired number of events
    events = []      # assemble data into events tuple (header,waveform)

    iev = 0
    while loop:

        if iev % 100 == 1:
            print 'reading event ',iev,'  pointer  ', pointer
        if lines[pointer] != marker or lines[pointer+1] != marker :   #   check the waveform record sentinel
            print 'read SSP, warning: event ',iev, 'incorrect record', lines[pointer:pointer+10]
            exit()
            
        head = []   # assemble the header, Manual Version 2.06

        for kk in range(nhead):
            #k = kk - pointer
            k = kk + pointer
            if kk % 2 == 1:    # assemble 16 bits words into 32,
                head.append(lines[k-1] + nsh*lines[k])

        rl = BitArray(uint=head[1], length=32)[16:32].uint   # record length
        ch = BitArray(uint=head[2], length=32)[12:16].uint   # chanel number

        if debug:
            print '  read_SSP , event number ', iev,' pointer  ',pointer, 'record length', rl, 2*rl+pointer, 'file length ',len(lines)
        
        ev_header = (ch)  # if no header requested, header consists of the channel number only 

        if get_header:

            peak_off = BitArray(uint=head[5], length=32)[0:8].uint
            peak_sum = BitArray(uint=head[5], length=32)[8:32].uint
    
            bas_sum = BitArray(uint=head[6], length=32)[8:32].uint
            integrated_sum_7_0 = BitArray(uint=head[6], length=32)[0:8].uint
    
            integrated_sum_23_8 = BitArray(uint=head[7], length=32)[16:32].uint
            baseline_offset = BitArray(uint=head[7], length=32)[0:16].uint
    
            cfd0 = BitArray(uint=head[8], length=32)[16:32].uint
            cfd1 = BitArray(uint=head[8], length=32)[0:16].uint
            cfd2 = BitArray(uint=head[9], length=32)[16:32].uint
            cfd3 = BitArray(uint=head[9], length=32)[0:16].uint
    
            local_ev_timestamp_15_0 = BitArray(uint=head[10], length=32)[0:16].uint
            fractional_timestamp = BitArray(uint=head[10], length=32)[16:32].uint
            local_ev_timestamp_47_16 = head[11]
    
            ev_header = (ch, peak_off, peak_sum, integrated_sum_7_0, bas_sum,
                         baseline_offset, integrated_sum_23_8,
                         cfd0, cfd1, cfd2, cfd3,
                         local_ev_timestamp_15_0, fractional_timestamp,
                         local_ev_timestamp_47_16)


        #  get the waveform
        
        wave = []

        #  check if the data is available  
        if pointer + 2*rl > nlines: break 
    
        for i in range(nhead, 2*rl):
            wave.append(BitArray(uint=int(lines[pointer+i]),
                                 length=16)[2:16].uint)
       
        evno += 1
        
        #  check for the end-of-reqested/available data   
        if evno > maxev:  #  all events?
            loop = False

        old_pointer = pointer
        pointer += 2*rl    #  pointer to nex event
        if debug:
            print 'check pointers', old_pointer, rl, pointer

        if pointer >= len(lines)-1:   # more daata exist?
            loop = False
        iev += 1
            
        if loop:
            if ( lines[pointer] != marker or lines[pointer+1] != marker  )  :

                print 'read_SSP, check structure, old pointer ', old_pointer, ' old  ',lines[old_pointer:old_pointer+10]
                print 'read_SSP, check structure, new/wrong pointer ', pointer, ' new  ',lines[pointer:pointer+10]
                for il in range(old_pointer+2,nlines):    # find the beginning of new event
                    if lines[il] == marker and lines[il+1]  == marker: break
                pointer = il    # re-adjusted pointer to the next event
                print 'read_SSP, check structure, adjusted pointer ', pointer, lines[pointer:pointer+10]
                wave = []  # empty waveform for incomplete evets
         
        events.append((ev_header, np.array(wave)))     

        
    return events
