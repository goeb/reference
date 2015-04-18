#!/usr/bin/python

import sys

progname = sys.argv.pop(0)
print "program name: ", progname

# the "usage" function
def usage() :
	print "Usage: ", progname, "[-h] [-a xxx] [-b yyy] file ..."
	sys.exit()

while len(sys.argv) :
	# get the first element of the remaining arguments
	arg = sys.argv.pop(0)
	if arg == "-h" :
		usage()
	elif arg == "-b" :
		b_arg = sys.argv.pop(0)
		print "option '-b' ", b_arg
	else :
		print "OTHER: ", arg

print "-- done --"
