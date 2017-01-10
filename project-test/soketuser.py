import socket

soks = socket.socket()
soks.bind(('',9080))
soks.listen(1)
conn , addr = soks.accept()

print('Успех:',addr)

while True:
    bind = conn,recv(1024)
    if not bind:
        break
    conn,send(bind.upper())

conn.close()
