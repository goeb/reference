import socket
import sys


class Tcpcat:
    def __init__(self):
        self.tx = 0
        self.rx = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        self.sock.connect((host, port))

    def send(self, data):
        self.sock.sendall("%d: %s\n" % (self.tx, data))
        self.tx += 1

    def recv(self, timeout):
        self.sock.settimeout(timeout)
        try:
            data = self.sock.recv(4096)
            self.rx += 1
        except socket.timeout:
            data = None

        return data

def main():
    tcpcat = Tcpcat()
    tcpcat.start("127.0.0.1", 2222)

    while True:
        msg = 'hello\n'
        sys.stdout.write("send:%d: %s" % (tcpcat.tx, msg))
        tcpcat.send(msg)
        data = tcpcat.recv(5)
        sys.stdout.write("recv:%d: %s\n" % (tcpcat.rx, data))

main()
