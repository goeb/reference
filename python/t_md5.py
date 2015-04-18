#!/usr/bin/python
import md5
import sys

s = sys.argv[1]
m = md5.md5(s)
print "md5(%s)=%s" % (s, m.hexdigest())
