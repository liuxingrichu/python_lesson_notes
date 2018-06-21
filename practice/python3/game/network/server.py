#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

server = socket.socket()
server.bind(('127.0.0.1', 1234))
server.listen(5)

while True:
    print('waiting for client ...')
    conn, addr = server.accept()
    print("client is coming from %s" % addr[0])
    cli_info = conn.recv(1024)
    print("client info: %s" % cli_info)
    conn.send(cli_info.upper())
server.close()