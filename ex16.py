#!/usr/bin/python

#import sys module
from sys import argv

# get filename as a command line argument
# argv[0] is the script name
# reference http://docs.python.org/library/sys.html
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "To erase file, hit RETURN."

raw_input("?")

print "Opening the file..."
# open file in write mode w instead of default read mode r.
# txt_file is a file object, not a string
txt_file = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncate statement isn't necessary.
# if a file already exists, opening it in write mode truncates the file.
# http://docs.python.org/library/functions.html?highlight=open#open
#txt_file.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

txt_file.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
txt_file.close()

