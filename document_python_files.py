#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Last edit: Sun May  9 21:11:40 CDT 2021

Created on Mon Dec 30 14:18:35 2019

@author: para

produce documnetation file for all python scripts ina directory
the defauls file name is python_docs.txt
"""

import re
import datetime
import os
from get_docstrings           import write_docstrings, module_docstrings

def document_python_files(code_dir, doc_dir):
    """
    list .py files and invoke print_doc for each of them
    """

    #  for every source file aqxtract docstrings into .py_doc file
    #  also extract the module dcstring into *.py_doc_module file
    
    files_documented = {}
    for file in os.listdir(code_dir):
        if file.endswith(".py"):
            
            fname = os.path.join(code_dir, file) 
            fp = open(fname)

            fnameo = doc_dir + '/' + file.replace('.py','.py_doc')
            print('   =====  source file ======', fname, '  docstring file ',  fnameo)           
            fo = open(fnameo,'w')
            
            fnameo_module = doc_dir + '/' + file.replace('.py','.py_doc_module')
            print('   =====  source file ======', fname, '  module docstring file ',  fnameo_module)           
            fm = open(fnameo_module,'w')       
            
            write_docstrings(fp, fo, fm)
            
            mod_dcrs = module_docstrings(fp)
            files_documented[file] = mod_dcrs

    #   order the source files by the development (last edit) history
    
    doc_time = {}
    dates = []
    
    for file in files_documented:

        docs_o = files_documented[file]
        
        #  remove whitespaces, newlines, etc
        docs = re.sub(' +',' ',docs_o)
        docs = docs.replace('\n',' ')
        tokens = docs.split(' ')

        #  make a imestamp for the last edit time
        sep = '-'
        date_str = tokens[5] + sep + tokens[2] + sep + tokens[3] + ' ' + tokens[4]
        date = datetime.datetime.strptime(date_str, '%Y-%b-%d %H:%M:%S')
        doc_time[(date,file)]  = (file,docs_o) 
        dates.append((date,file))
        
    dates = sorted(dates, reverse=True)

    #  proint the time-ordered file list
    
    for it in dates:
        print ('   ==========>   ',it[1])
        print ('   last edit  ', it[0])
        print ( '   ')
        print (files_documented[it[1]])
        print ( '   ')
    
def history_python_files(code_dir, doc_dir):
    """
    list .py files, extract the last edit files and create time orderd list of modules
    """

    for file in os.listdir(code_dir):
        if file.endswith(".py"):
            
            fname = os.path.join(code_dir, file) 
            fp = open(fname)

            fnameo = doc_dir + '/' + file.replace('.py','.py_doc')
            print('   =====  source file ======', fname, '  docstring file ',  fnameo)           
            fo = open(fnameo,'w')
            
            fnameo_module = doc_dir + '/' + file.replace('.py','.py_doc_module')
            print('   =====  source file ======', fname, '  module docstring file ',  fnameo_module)           
            fm = open(fnameo_module,'w')       
            
            write_docstrings(fp, fo, fm)
            mod_dcrs = module_docstrings(fp)
            
            print (mod_dcrs)
                        
if __name__ == '__main__':
    import sys

    #  as a default document files in the current directory
    #  unless a code directory is passed as an argument
    #  the documentation files are written to a subdirectory /pyt_doc of the source directory
    
    if len(sys.argv) > 1:
        code_dir = sys.argv[1]
    else:
        print('document_python_files invoked with no directory, current directory used')
        code_dir = './'
        
    print('generate documentation of python files in directory ', code_dir)

    doc_dir = code_dir + 'pyt_doc'  
    print('generate documentation of python files in directory ', code_dir)    
    print('documentation saved in  in directory ', code_dir)    
    if os.path.isdir(doc_dir):
        pass
    else:
        os.mkdir(doc_dir)

    document_python_files(code_dir, doc_dir)  
