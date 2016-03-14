#!/usr/bin/env python

#this on is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# This just takes on argument
def print_one(arg1):
    print("arg1: %r" %arg1)

#this on takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Nerdy","Davvi")
print_two_again("Nerdy","Davvi")
print_one("First!")
print_none()
