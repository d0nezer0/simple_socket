#!/usr/bin/env python

import socket
from threading import Thread

HOST = 'localhost'
PORT = 12345
BUFSIZE = 2014


def client_handle(client_socket):

    client_info = str(client_socket.getpeername())
    print "Got connection from %s" % client_info

    while True:
        data = client_socket.recv(BUFSIZE)
        if not data:
            print 'missed a message!!!'
            continue
        else:
            print data
            # admin_message = raw_input('admin says: ')
            # if admin_message:
            #     client_socket.sendall('admin says: ' + admin_message)
            # else:
            #     client_socket.sendall('message received!')
            client_socket.sendall('message received from %s!' % client_info)

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
