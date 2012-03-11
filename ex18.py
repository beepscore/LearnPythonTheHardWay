#!/usr/bin/python

# this one is like your scripts with argv
def print_two(*args):
    print "args[0]: %r, args[1]: %r" % (args[0], args[1])
    #In Python can assign multiple variables from one array on one line
    # assign arg0 and arg1 using array "args"
    arg0, arg1 = args
    print "arg0: %r, arg1: %r" % (arg0, arg1)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg0, arg1):
    print "arg0: %r, arg1: %r" % (arg0, arg1)

# this takes one argument
def print_one(arg0):
    print "arg0: %r" % arg0

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
