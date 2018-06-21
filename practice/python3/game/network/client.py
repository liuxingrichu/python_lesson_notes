import socket

client = socket.socket()
client.connect(('localhost', 1234))
client.send('hello, world'.encode('utf-8'))
data = client.recv(1024)
print(data.decode('utf-8'))
client.close()