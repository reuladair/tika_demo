#!/usr/bin/env python
 
## =============================================================
## Created Sunday, July 16, 2017 at 13:49:50 (spinor@yahoo.com)
## Copyright (C) 2017, by Reuladair Fear. All Rights Reserved.
## =============================================================
 
##
## standard package imports
##
 
import os
import sys
import time
import tika
import numpy as np
from tika import parser

## summarize the contents of a text buffer

def summarize(name, text_buffer):
    '''
    '''
    print("%s:" % name)
    file_bytes = len(text_buffer)
    lines_in_file = (text_buffer).split('\n')
    file_words = 0
    words = []
    for line in lines_in_file:
        words_in_line = line.split(' ')
        for w in words_in_line:
            words.append(w)
    file_words = len(words)
    uniq_words = len(np.unique(words))
    file_lines = len(lines_in_file)
    print("summary:")
    print("\tbytes = %d" % file_bytes)
    print("\twords = %d (%d unique)" % (file_words, uniq_words))
    print("\tlines = %d" % file_lines)
    return

if(__name__ == "__main__"):
   '''
   
   '''
   if (os.getenv('TIKA_SERVER') == None):
       ## well we can't find an env-var pointing to a server...
       raise OSError("tika_demo: TIKA_SERVER is undefined")
   else:
       ## found env-var that is supposed to point to TIKA...
       tika_server = ("%s/tika" % os.getenv('TIKA_SERVER'))
       print("TIKA_SERVER=\'%s\'" % tika_server)

       ## okay we have the server, make sure we've been given either
       ## a directory or a file...
       if (len(sys.argv) != 2):
           ## need more arguments that this...
           raise OSError("tika_demo:  must supply either file, directory, or string")
       else:
           ## we we have something... let's figure out what it is...
           if ((os.path.exists(sys.argv[1]) == True) and
               (os.path.isfile(sys.argv[1]) == True)):
               ## okay it's a FILE...
               parsed = parser.from_file(sys.argv[1], tika_server)
               ## the metadata about the file...
               print(parsed["metadata"])
               ## we assume the file is long so we won't print it all out...
               summarize(sys.argv[1], parsed["content"])
           elif ((os.path.exists(sys.argv[1]) == True) and
                 (os.path.isdir(sys.argv[1])  == True)):
               ## okay it's a DIRECTORY...
               file_list = os.listdir(sys.argv[1])
               for a_file in file_list:
                   ## build a complete file name...
                   full_name = ("%s/%s" % (sys.argv[1], a_file))
                   ## well okay, it appears to be a file...
                   parsed = parser.from_file(full_name, tika_server)
                   ## the metadata about the file...
                   print(parsed["metadata"])
                   ## we assume the file is long so we won't print it all out...
                   summarize(full_name, parsed["content"])
           else:
               ## it's a STRING...
               parsed = parser.from_buffer(sys.argv[1], tika_server)
               ## the metadata about the string...
               print(parsed["metadata"])
               ## we'll just assume it's short and print it out...
               print(parsed["content"])

   # okay...
   

           






 
 
