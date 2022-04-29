#!/usr/bin/env python3

#Author: Ashley Bryant
#Description:

import socket
import sys

LHOST = ''
LPORT = 5042
RCV_DATA = ""

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while 1:
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print('Connected by ', addr)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        print(f"The server received this data:{RCV_DATA}")
        myFile = (RCV_DATA).decode("utf-8")
        with open("transferFile.txt", 'w') as f:
            f.write(myFile)
            print("Transferred data stored in transferFile.txt")
        L_CONN.sendall(RCV_DATA)


    L_CONN.close()
