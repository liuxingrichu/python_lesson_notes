import socket

client = socket.socket()
client.connect(('localhost', 8888))

while True:
    cmd = input('>> ').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()