#!/usr/bin/env python

import socket
from threading import Thread

host = "192.168.1.17"
port = 12345


def handlechild(clientsock):

    client_info = str(clientsock.getpeername())
    print "Got connection from %s" % client_info
    while True:
        data = clientsock.recv(1024)
        if not len(data):
            break
        print data
        clientsock.sendall(client_info)
    print 'close %s connection.' % client_info
   #  clientsock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(1)

while True:
    print 'waiting for connection...'
    try:
        client_sock, client_addr = sock.accept()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        print 'exception: ', e
        continue

    t = Thread(target=handlechild, args=[client_sock])
    t.setDaemon(1)
    t.start()

