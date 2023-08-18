#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:24:23 2020

@author: para
create a web page with a list of files of a certain type
for some file types create a documentation html file, assuming some rules:
    .C files - root macros. functions starting in the first column f
               followed by the description starting with '//' in the first column
               and ending with bare '//'


"""
from __future__ import print_function

import os


def file_cont(file,filetype):
    """
    extract the content of the file to display in the firectory file
    """

    print(('  create the doumentation page for file ', file,  'file type ', filetype  ))    
    cont = ''                    # content of the docmentation file 
    function_list = []           # list of functions present in a file
    
    indent = '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'    # indetation of the descritption lines
    head_fun     = '<h3 style="color:red">'      # Header level for the function
    end_head_fun = '</h3>'        

    lines= open(file).readlines()
        
    if filetype == 'C':
       
        line_doc = False    # documentation line?
        line_fun = False    # function definition line?
        
        for ll in lines:
            line = ll.rstrip()               # ignore trailing whitespaces 
            if len(line) == 0: continue      # ignore empty lines
     
            #   ----  find the function header: anything in fisrt column but '/'    
            if line[0] != ' ' and line[0] !='/':
                line_fun = True
                header = head_fun            
                #  parse the first line to identify the function name
                fun_line = ' '.join(line.split())
                fun_name = fun_line.split('(')[0].split(' ')[1] 
                function_list.append(fun_name)
               
            if line_fun :
                header += line

            #    ---- function definition ends with ')'      
            if line_fun  and line[-1] == ')':

                header +=  end_head_fun 
                header = ' '.join(header.split())

                #    parse the function definition to identify all arguments                
                tok1 = header.split('(')
                head_item = tok1[0] + end_head_fun + '\n <ul>\n'
                
                #   find arguments
                tok12 = tok1[1].split(')')

                if len(tok12[0]) > 0:
                    tok2 = tok12[0].split(',')
                    if len(tok2) > 0:
                        for args in tok2:
                            arg = args.replace(')','').lstrip().split(' ')
                            head_item += '<li> <i>' + arg[0] + '</i> <b>'   + arg[1] + '</b></li>\n'
                        head_item += '</ul>\n'
                        cont += head_item            
                
                print(('=======   header ',head_item))
                line_fun = False
                
    
     
            #   find function description           
    
            if line[0:2] == '//':
                line_doc = True
                cont += '<p>' 
    
            if line[0:2] == '//' and len(line) == 2:
                cont += '</p>' 
                line_doc = False
                
            if line_doc :
                cont += indent + line 
                

       
    return cont, function_list
            
def dir_page(directory, filetype):
    
    web_page_file = directory + '/dir_list_' + filetype + '.html'
    print (web_page_file)
    fo = open(web_page_file,'w')
    
    header = '''
    <!doctype html>
    <title>Path: ''' + directory + '''</title>
    <h1>  List of files of type ''' + filetype + ' in ' + directory + '''</h1>
    <ul>'''

    fo.write (header)
#
#{%- for item in tree.children recursive %}
#    <li>{{ item.name }}
#    {%- if item.children -%}
#        <ul>{{ loop(item.children) }}</ul>
#    {%- endif %}</li>
#{%- endfor %}
    


    filelist = os.listdir(directory)

    functions = {}     #  find all functions, report occurencies
    
    for filename in filelist:
        if filename.endswith(filetype):
            file_doc = 'doc/' + filename.replace('.C','.html')
            print (filename)
            print(('++++++++++++++++++++++',file_doc))
            file_line = '<li><a href="'+ file_doc + '">' + filename + '</a></li>\n'
            fo.write (file_line)
            
            #   file-specific documentation page
            cont = '''
            <!doctype html>
            <title>Macro File  ''' + filename + '''</title>
            <h1>  File ''' + filename + ''' List of macros ''' + '''</h1>
            <ul>'''
            
            file_page, functions_present = file_cont(directory + '/' + filename, filetype)
            cont += file_page
            cont += '</ul> '
            fun_file = open(file_doc,'w')
            #print (filename, cont)
            fun_file.write(cont)
            fun_file.close()
            
            for fun in functions_present:
                if fun not in functions:
                    functions[fun] = []
                    
                functions[fun].append(filename)
            
    fo.write ('</ul>')
    fo.close()

    f_list = [f for f in functions]
    f_list.sort()
    
    fun_rep = directory + '/function_rep.html'
    ff = open(fun_rep,'w')
    
    fun_header = '''
    <!doctype html>
    <title>Functions in ''' + directory + '''</title>
    <h1>  List of functions '''  + '''</h1>
    <ul>'''

    ff.write (fun_header)

    
    for fun in f_list:
        print(('-----   ',fun))
        print(('               ',functions[fun]))        
        fun_it = '<li>' + fun + '</li> \n <ul>'
        ff.write(fun_it)
        for ffile in functions[fun]:
            fun_inst = '<li>' + ffile +'</li>'
            ff.write(fun_inst)
        ff.write('</ul>')
if __name__ == '__main__':
    directory = '/Users/para/root_macros'
    filetype = 'C'
    dir_page(directory, filetype)