#!/usr/bin/python

# References
# python raw input
# http://docs.python.org/library/functions.html

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight)
# use %s format specifier to suppress printing escape characters
print "So, you're %s old, %s tall and %s heavy." % (
        age, height, weight)

