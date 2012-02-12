#!/usr/bin/python

# References
# python escape sequences
# http://docs.python.org/reference/lexical_analysis.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    """


# When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string.
print "%r" % tabby_cat
print tabby_cat
print "%r" % persian_cat
print persian_cat
print "%r" % backslash_cat
print backslash_cat
print "%r" % fat_cat
print fat_cat

