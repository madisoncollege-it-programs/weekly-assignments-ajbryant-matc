#!/usr/bin/env python3

#Author: Ashley Bryant
#Purpose:

import socket

RHOST    = '127.0.0.1'
RPORT    = 5000


RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

C_SOCK.connect((RHOST, RPORT))
while True:
    i = input("Enter your input: ('E' to exit)  ")
    if i == 'E':
        break

    C_SOCK.send(bytearray(i,'utf8'))

    RCV_DATA = C_SOCK.recv(1024)

    print(RCV_DATA.decode())

C_SOCK.close()
