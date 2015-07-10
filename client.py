#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
import os
from Queue import Queue

HOST = 'localhost'
PORT = 12345
BUFSIZE = 512
ADDR = (HOST, PORT)

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ADDR)

name = raw_input('who are you :')
if not name:
    name = 'anonymous user'
send_data = '%s has joined ...' % name
tcp_client.send(send_data)

while True:
    data = raw_input('>')
    if not data:
        continue
    if len(data) > BUFSIZE:
        print 'You can send %s bytes below' % BUFSIZE
        continue
    send_data = name + ' says: ' + data
    tcp_client.send(send_data)

    server_data = tcp_client.recv(BUFSIZE)

    if not server_data:
        print 'missed a message!!!'
        continue
    else:
        print server_data

tcp_client.close()
