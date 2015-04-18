
import re
import serial
#import Logger
import select
import sys
import time

class Logger:
    def log(self, msg):
        msg = msg.strip()
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        sys.stdout.write(t + ' ' + msg + '\n')

LOG = Logger()

class Serial:

    def __init__(self, device, bitrate):
        self.fd = serial.Serial(device, bitrate, timeout=0)

    def write(self, data):
        LOG.log('serial-tx: %s' % (data))
        self.fd.write(data)

    def writeLn(self, data):
        self.write(data)
        self.fd.write('\n')

    def recv(self, timeout):
        "Simple read, with timeout in seconds"
        line = ''
        data = ''
        t0 = time.time()
        while True:
            remaining = timeout - (time.time() - t0)
            if (remaining < 0):
                LOG.log('serial: timeout')
                break

            select.select([self.fd.fileno()], [], [], remaining)
            char = self.fd.read()
            line += char
            data += char
            if char == '\n':
                LOG.log('serial-rx: %s' % (line))
                line = ''

        return data

    def recvUntil(self, patterns, timeout):
        "read until a pattern is found, with timeout in seconds"
        line = ''
        t0 = time.time()
        result = None # re.match object
        if type(patterns)==str: patterns = [patterns]

        while True:
            remaining = timeout - (time.time() - t0)
            if (remaining < 0):
                LOG.log('serial: timeout')
                break

            select.select([self.fd.fileno()], [], [], remaining)
            char = self.fd.read()

            if char == '\n':
                line = line.strip() # remove possible \r
                LOG.log('serial-rx: %s' % (line))
                # check if line matches
                for p in patterns:
                    LOG.log("result = re.search(%s, %s)" %(p, line))
                    result = re.search(p, line)
                    if result is not None: return result
                line = ''

            else:
                line += char

        return result

        
# test

s = Serial('/tmp/x', 115200)

s.recvUntil('XX', 10)
s.writeLn("HELLO")
m = s.recvUntil(['toto(.)(.)', 'tata(.)'], 15)
LOG.log("m=%s" % m)
if m is not None:
    LOG.log("m.string=%s" % (m.string) )
    LOG.log("m.groups=%s" % m.groups().__repr__())



