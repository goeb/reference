#!/usr/bin/python

import os

xin, xout, xerr = os.popen3("ls kzef")
xin.write("leqksj;")
xin.close()
print "stdout:"
print xout.read()
print "--"
print "stderr:"
print xerr.read()
print "--"
