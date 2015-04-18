import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 2222))
s.send("hello")
x = s.recv(10)
print x
