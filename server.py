#!/usr/bin/env python

import socket
from threading import Thread

HOST = "192.168.1.17"
PORT = 12345


def client_handle(client_socket):

    client_info = str(client_socket.getpeername())
    print "Got connection from %s" % client_info
    while True:
        data = client_socket.recv(1024)
        if not len(data):
            break
        print data
        client_socket.sendall(client_info)
    print 'close %s connection.' % client_info
    # client_socket.close()


# define socket type, TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set options on the socket.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

while True:
    print 'waiting for connection...'
    try:
        client_sock, client_addr = sock.accept()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        print 'exception: ', e
        continue

    t = Thread(target=client_handle, args=[client_sock])
    t.setDaemon(1)
    t.start()
