#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import handle


def handle_request(client):
    client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
    f = open('index.html', 'r')
    data = f.read()
    f.close()
    name = handle.choice_student()[1]
    data = data.replace('@@@@@', name)
    client.send(bytes(data, encoding='utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8888))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
       			

if __name__ == '__main__':
    main()
