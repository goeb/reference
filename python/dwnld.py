#!/usr/bin/python

import sys
import os

min = int(sys.argv[1])
n = int(sys.argv[2])
base_url = sys.argv[3]

print "--------"
print "min=", min
print "n=", n
print "base_url=", base_url
print "--------"

def new_dir() :
	x = 0
	base_dirname = "dir_%04d"
	while os.path.exists( base_dirname % x ) :
		x = x+1
	return base_dirname % x

dir = new_dir()
os.mkdir(dir)


for i in range(min, min+n):
	url = base_url % i
	file = os.path.basename(url)
	cmd = 'wget -O %s/%s %s' % ( dir, file, url)
	print "cmd=", cmd
	os.system(cmd)
