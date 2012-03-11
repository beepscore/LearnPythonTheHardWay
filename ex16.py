#!/usr/bin/python

#import sys module
from sys import argv

# get filename as a command line argument
# argv[0] is the script name
# reference http://docs.python.org/library/sys.html
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# note txt_file is a file object, not a string
txt_file = open(filename, 'w')

print "Truncating the file. Goodbye!"
txt_file.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

txt_file.write(line1)
txt_file.write("\n")
txt_file.write(line2)
txt_file.write("\n")
txt_file.write(line3)
txt_file.write("\n")

print "And finally, we close it."
txt_file.close()

