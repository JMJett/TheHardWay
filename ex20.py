__author__ = 'Jarod Jett'

from sys import argv

script, input_file = argv

def file_len(fname):
    current_file = open(input_file)
    for i, l in enumerate(current_file):
        pass
    return i + 2

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print 3 lines\n"

for i in range(1,4):
    current_line = i
    print_a_line(current_line, current_file)

rewind(current_file)


print "Let's make a general case to print line by line until the end:\n"

for i in range(1, file_len(current_file)):
    current_line = i
    print_a_line(current_line, current_file)
