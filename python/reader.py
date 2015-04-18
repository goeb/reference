
import os

f = os.open("/home/fred/tmp/fred_fifo", os.O_RDONLY)

line = os.read(f, 10)
while line != '':
	print "line read: " + line
	line = os.read(f, 10)


