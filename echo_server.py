# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:46:44 2017

@author: Brian
"""

import socket
import sys
import json    

class ServerClass(object):
    def __init__(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the port
        server_address = ('localhost', 10000)
        print('starting up on %s port %s' % server_address)
        sock.bind(server_address)
        
        # Listen for incoming connections
        sock.listen(1)
        
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            
            try:
                print('connection from', client_address)
        
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(4096)
                    print('received "%s"' % data)
                    if data:
                        print(data.decode())
                        data = json.loads(data.decode().replace("'","\""))
                        func = getattr(self, data['fxn'])
                        out = func(data['x'], data['y']) 
                        print('output calculated, sending back to the client')
                        connection.sendall(str(out).encode())
                    else:
                        print('no more data from', client_address)
                        break
                    
            finally:
                # Clean up the connection
                connection.close()
        
    def add(self,x,y):
        return x+y
    
    def mult(self,x,y):
        return x*y
                
if __name__ == "__main__":
    ServerClass()