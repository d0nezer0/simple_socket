#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
import os
from Queue import Queue

HOST = '192.168.1.17'
PORT = 12345
BUFSIZE = 512
ADDR = (HOST, PORT)

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        continue
    tcp_client.send(data)
    data = tcp_client.recv(BUFSIZE)

    if not data:
        break
    print data

tcp_client.close()
