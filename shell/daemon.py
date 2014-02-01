
import sys
import time
f = open(sys.argv[1])

while True:
    line = f.readline()
    if line == '': time.sleep(1)
    print "daemon: line=", line
    if line.strip() == 'STOP':
        print 'stopping...'
        sys.exit(1)
