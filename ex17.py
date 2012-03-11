#!/usr/bin/python

#import sys module
from sys import argv
# exists returns True if a file exists
from os.path import exists

# assign "from_file" and "to_file" using command line array argument "argv"
#from_file = argv[0]
#to_file = argv[1]
#In Python can assign multiple variables from one array on one line
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# As of Python 2.5, call "with", then don't need to explicitly call
# "close"
# http://stackoverflow.com/questions/4599980/python-close-file-descriptor-question
# closing files frees up memory sooner than the garbage collector
# closing files prevents running out of file handles.
# http://docs.python.org/library/stdtypes.html?highlight=close#file.close
with open(from_file) as input:
    indata = input.read()
    print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

output = open(to_file, 'w')
output.write(indata)

output.close()
