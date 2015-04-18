#!/usr/bin/python
#
# usage: $0 file.hpp
# generates 2 files for UT stubs


import popen2
import sys
import re

file = sys.argv[1]
print "Input:", file

# the cpp processing does the following:
# - remove comments
# - remove macros (except #include, see below)
# - do not include files (because there is no -I argument)
# - keep #include directives
cmd = "cpp  -dI -P " + file
(stdout, stdin, stderr) = popen2.popen3(cmd)

hpp_buffer = ''
cpp_buffer = ''

def printHPP(line) :
	global is_private, hpp_buffer
	if not is_private :
		hpp_buffer = hpp_buffer + line + '\n'

def printCPP(line) :
	global is_private, cpp_buffer
	if not is_private :
		cpp_buffer = cpp_buffer + line + '\n'

class_name = None
is_in_class = False
is_private = False
line = stdout.readline();
while line != "" :
	line = line.strip();
	if re.match("^static", line) :
		None
	elif re.match("^class\s", line) :
		class_name = re.sub("class\s*(\\w*)\\W.*", "\\1", line)
		print "class_name=", class_name
		is_in_class = True
		printHPP(line)
		is_private = True
	elif re.match("^public\s*:", line) :
		is_private = False
		printHPP(line)
	elif re.match("^protected\s*:", line) :
		is_private = False
		printHPP(line)
		printCPP(line)
	elif re.match("^private\s*:", line) :
		is_private = True
	elif re.search("\(", line) : # prototype of a method
		printHPP(line)
		cpp_line = re.sub("(\w*\s*\()", class_name+"::\\1", line)
		cpp_line = re.sub("\)\s*;$", ") {\n\n}", cpp_line)
		printCPP(cpp_line)
	elif re.match("^}\s*;", line) : # end of class
		is_private = False
		is_in_class = False
		printHPP(line)
	elif re.match("^#include", line) :
		printHPP(line)
	elif line == '' :
		None
	else :
		printHPP(line)
		if not is_in_class :
			printCPP(line)

	# read the next line
	line = stdout.readline();



# decoration for hpp file
print "-------- HPP file --------"
print "#ifndef " + class_name + "_hpp_"
print "#define " + class_name + "_hpp_"
print hpp_buffer
print "#endif"


# decoration for cpp file
print "-------- CPP file --------"
print '#include "' + class_name + '.hpp"'
print cpp_buffer

