#!/usr/bin/python

#import sys module
from sys import argv
# exists returns True if a file exists
from os.path import exists

#assign value to to_file
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

output = open(to_file, 'w')
output.write(indata)

output.close()
input.close()
