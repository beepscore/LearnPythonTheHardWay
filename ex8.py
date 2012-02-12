#!/usr/bin/python

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
# output surrounds each word with ' '
print formatter % ("one", "two", "three", "four")

print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# third string will be delimited by "" due to inner '
print formatter % (
        "I had this thing.", 
        "That you could type up right.", 
        "But it didn't sing.",
        "So I said goodnight."
        )

