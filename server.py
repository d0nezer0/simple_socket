#!/usr/bin/env python

import socket
import select
from threading import Thread

HOST = 'localhost'
PORT = 12345
BUFSIZE = 2014


# send a broadcast message beside server and the client where message from
def broadcast_data(sock_from, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock_from:
            try:
                socket.send(message)
            except Exception, e:
                print 'socket disconnect, ', e
                socket.close()
                CONNECTION_LIST.remove(socket)


if __name__ == '__main__':

    CONNECTION_LIST = []

    # define socket type, TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set options on the socket.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)

    print "Chat server started on port " + str(PORT)

    while True:

        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for socket in read_sockets:

            # this is the new socket just connected.
            if socket == server_socket:
                client_sock, client_addr = server_socket.accept()
                CONNECTION_LIST.append(client_sock)
                print 'Client [%s:%s] connected' % client_addr
                broadcast_data(client_sock, '[%s:%s] enter the room\n' % client_addr)
            # get message if has, and send to broadcast.
            else:
                try:
                    data = socket.recv(BUFSIZE)
                    print ''
                    if data:
                        broadcast_data(socket, '')
                except:
                    broadcast_data(socket, '')
                    print 'Client (%s, %s) is offline' % client_addr
                    socket.close()
                    CONNECTION_LIST.remove(socket)
                    continue

    server_socket.close()
