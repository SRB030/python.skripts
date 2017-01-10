import socket

soks = socket.socket()
soks.connect(('localhost',9080))
soks.send('Привет')

bind = soks.recv(1024)
soks.close()

print(bind)