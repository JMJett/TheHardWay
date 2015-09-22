__author__ = 'Jarod Jett'

#Similar to passing arguments to scripts via argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#You can do that way better:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

print_two("Jarod", "Jett")
print_two_again("Jarod","Jett")
print_one("One time!")