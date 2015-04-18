import threading
import sys
import time

def log(msg):
    sys.stdout.write(msg + "\n")

class Fthread:
    def __init__(self, name):
        self.name = name

    def log(self, msg):
        sys.stdout.write(self.name +': ' + msg + "\n")

    def start(self):
        self.log("Thread starting...")
        self.thread = threading.Thread(None, self.run, None)
        self.thread.start()


    def run(self):
        self.log("Thread running...")
        time.sleep(5)
        self.log("Thread ending...")
        

    def stop(self):
        self.log("stop!")



# main
A = Fthread('A')

log('active_count=' + str(threading.active_count()))
A.start()
log('active_count=' + str(threading.active_count()))

A.stop()
log('active_count=' + str(threading.active_count()))

A.thread.join(3)

# master.send('xxx')
# slave.send('get abc')
# rsp = slave.recv()
# assert(contains(rsp, "Alarm: 0"))
