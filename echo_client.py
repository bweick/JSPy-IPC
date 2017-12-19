# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:46:47 2017

@author: Brian
"""

#! /usr/bin/env python
import socket
import time
import sys
import json
from subprocess import Popen

class ClientCall(object):

    def __init__(self):

        host = 'localhost'
        eth_port = 8545
        self._js_port = 10000

        self._eth_node = Popen('node eth_server.js %s %s' %(host, str(eth_port)))

        def check_server():
            try:
                self.run_process('testConnection')
            except:
                check_server()

        check_server()

        #self._js_serv = Popen('node echo_server.js %s %s' %(host, str(self._js_port)))

    def run_process(self, fxn, params={}):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self._js_port)
        print(sys.stderr, 'connecting to %s port %s' % server_address)
        sock.connect(server_address)

        try:
            # Send data
            message = {"fxn": fxn,
                       "vars": params
                       }

            print(sys.stderr, message)
            sock.sendall(str(message).encode())

            data = sock.recv(4096)
            data = data.decode()
            #data =  json.loads(data.decode().replace("'","\""))
            print(data)

        finally:
            print(sys.stderr, 'closing socket')
            sock.close()

    def kill_process(self):
        self._eth_node.kill()
        #self._js_serv.kill()

if __name__ == "__main__":
    call = ClientCall()

    call.run_process('zrxAddress')
    call.run_process('nullAddress')
    call.run_process('salt')
    print("killing server...")
    call.kill_process()
    print("server killed.")
