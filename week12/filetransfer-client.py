#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Open a file, read it to a variable, and send to the server.

import socket

RHOST = '127.0.0.1'
RPORT = 5042


with open('filefornetworksocket.txt', 'r') as f:
        myFile = f.read()

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
C_SOCK.send(bytearray(myFile,'utf8'))

RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA)

C_SOCK.close()

