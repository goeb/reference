#!/usr/bin/python

import os
import sys

# create a directory
test_dir = "test_dir"
n = 1
#filename=test_dir+"."+str(n)
if os.access(test_dir, os.F_OK) == True :
	print "File already existing: ", test_dir
	print "Exiting..."
	sys.exit(1)

# mkdir ...  drwxr-xr-x
rc = os.mkdir(test_dir, 0755)
os.chdir(test_dir)
