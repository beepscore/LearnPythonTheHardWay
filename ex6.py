#!/usr/bin/python

# References
# string formatting
# http://docs.python.org/library/stdtypes.html

# put string in string #6 (converts int to string)
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# put string in string #1, #2
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# use %r format specifier. It puts the value of x within ' '
# put string in string #3
print "I said: %r." % x
# put string in string #4
print "I also said: '%s'." % y

hilarious = False
# put string in string #5 (converts bool to string)
joke_evaluation = "Isn't that joke so funny?! %r"

# joke_evaluation contains format specifier, 
# so it works with % hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenate strings
print w + e
