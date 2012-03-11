#!/usr/bin/python

# this one is like your scripts with argv
def print_two(*args):
    print "args[0]: %r, args[1]: %r" % (args[0], args[1])
    #In Python can assign multiple variables from one array on one line
    # assign arg1 and arg2 using array "args"
    # These names are confusing! arg1 == args[0] and arg2 == args[1]
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
