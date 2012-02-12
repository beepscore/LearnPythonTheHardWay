#!/usr/bin/python

#import sys module
from sys import argv

# get filename as a command line argument
# advantage- can be supplied programmatically, doesn't require user input
# argv[0] is the script name
# reference http://docs.python.org/library/sys.html
script, filename = argv

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# get filename from user input
# advantage- user can choose file at runtime.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()

#to open python from command line and read file:
#$ python
#>>> textfile = open('ex15_sample.txt')
#>>> print textfile.read()
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.
#>>> textfile.close()
#>>> quit()
