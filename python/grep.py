#!/usr/bin/python

# this program is like 'grep'
# regular expression may be used

import sys
import re

argv = sys.argv
progname = argv.pop(0)
if len(argv)>=1 :
	pattern = argv.pop(0)
else :
	print "usage:", progname, "pattern [ file ]"
	sys.exit(1)

if len(argv)>=1 :
	filename=argv.pop(0)
	input = open(filename, "r")
else :
	input = sys.stdin

line = input.readline()

while line != "" :
	if line[-1]=='\n' :
		line = line[:-1]
	if None != re.search(pattern, line) :
		print line
	line = input.readline()
