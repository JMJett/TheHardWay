__author__ = 'Triphos'

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL + C"
print "If you're okay with it press enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm writing these lines to the file."

target.write("%s\n%s\n%s\n" %(line1, line2, line3))
target.close()

print "Now I'm going to read out the lines to prove they wrote to the file: "
target = open(filename)
print target.read()

print "And finally, we close the file."
target.close()

