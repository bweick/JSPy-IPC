# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:46:47 2017

@author: Brian
"""

#! /usr/bin/env python
import socket
import sys
import json
from subprocess import Popen
from multiprocessing import Process

class ClientCall(object):

    def __init__(self):
        self.p = Popen('node echo_server.js')

    def run_process(self, fxn, x, y):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print(sys.stderr, 'connecting to %s port %s' % server_address)
        sock.connect(server_address)

        try:

            # Send data
            message = {"fxn": fxn,
                       "x": x,
                       "y": y}

            print(sys.stderr, message)
            sock.sendall(str(message).encode())

            data = sock.recv(4096)
            data = data = json.loads(data.decode().replace("'","\""))
            #print(sys.stderr, 'received "%s"' % int(data.decode()))
            print(data)

        finally:
            print(sys.stderr, 'closing socket')
            sock.close()

if __name__ == "__main__":
    call = ClientCall()

    call.run_process('mult', 4, 10)
    call.run_process('add', 5, 6)
    print("killing server...")
    call.p.kill()
    print("server killed.")
