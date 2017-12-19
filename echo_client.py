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
                self._run_process('testConnection')
            except:
                check_server()

        check_server()

        #self._js_serv = Popen('node echo_server.js %s %s' %(host, str(self._js_port)))

    def _run_process(self, fxn, params={}):
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

    def get_salt(self):
        self._run_process('salt')

    def get_null_address(self):
        self._run_process('nullAddress')

    def get_zrx_address(self):
        self._run_process('zrxAddress')

    def kill_process(self):
        self._eth_node.kill()
        #self._js_serv.kill()

if __name__ == "__main__":
    call = ClientCall()

    call.get_zrx_address()
    call.get_null_address()
    call.get_salt()
    print("killing server...")
    call.kill_process()
    print("server killed.")
