#!/usr/bin/python

# References
# string formatting
# http://docs.python.org/library/stdtypes.html
# python doesn't have constants. You can make a read-only property.
# http://stackoverflow.com/questions/2682745/creating-constant-in-python
LBM_PER_KG = 2.204

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight_lb = 180 # lbs
eye_color = 'Blue'
teeth = 'White'
hair_color = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight_lb
print "He's %g kilograms heavy." % (weight_lb / LBM_PER_KG)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eye_color, hair_color)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight_lb, age + height + weight_lb)
