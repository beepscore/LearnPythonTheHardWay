#!/usr/bin/python

# References
# python raw input
# http://docs.python.org/library/functions.html

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight)
# use %s format specifier to suppress printing escape characters
print "So, you're %s old, %s tall and %s heavy." % (
        age, height, weight)

