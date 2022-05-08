#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Demonstrate competency in creating a variety of functions.

import json
import requests
import socket
import argparse
import subprocess
import sys
import bs4


myDict = dict()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments')

    parser.add_argument('-i', '--ipaddress', dest='varString', type=str, default='Hello', required=True, help='Enter an ip address')
    parser.add_argument('-f', '--function', dest='varInteger', type=int, default=10.0, required=True, help='Enter the function number (1, 2, 3, 4, 5)')

    myIp = ((parser.parse_args()).varString)
    myFunc = ((parser.parse_args()).varInteger)

    url = f'http://{myIp}/q{myFunc}'

print(f'Name: Ashley Bryant')
print(url)


if myFunc == 1:
#    def get_response(response):
        response = requests.get(url)
        print("ANSWER:", response.text)
 #       return myText
#-----------------------------------------------------------------------------

if myFunc == 2:
#    def parse_string(str):
        res = requests.get(url)
        res.raise_for_status()

        mySoup = bs4.BeautifulSoup(res.text,features='html.parser')

        elems = mySoup.select('H3')
        strTag = str(elems)
        str1 = (strTag[9:27:2])
        str2 = ' ''Ashley'
        print("ANSWER:",(str1) + (str2))
#----------------------------------------------------------------------------

if myFunc == 3:
   # def parse_header():
    response = requests.get(url)
    if response.ok:
        for key, value in response.headers.items():
           if key == 'MATC-HEADER':
             print("ANSWER:",value)


#--------------------------------------------------------------------------

if myFunc == 4:
#    def parse_json(varPub):
        response = requests.get(url)
        json_dict = json.loads(response.text)
        json_string = json.dumps(json_dict)
        print(json_string)
        for publisher in json_string:
            print('publisher')
#        print(json_dict.values())
#        dumps_dict = (json.dumps(json_dict))

#        for key, value in json_dict:
        #for 'Music and Books' in json_dict:
 #           print({key})
#-----------------------------------------------------------------------
if myFunc == 5:
    def socket_client(myIp):

        RHOST = {myIp}
        RPORTS = range(5000,6000)
        myTimeout = 2

        for RPORT in RPORTS:
             C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             C_SOCK.settimeout(myTimeout)

        try:
             C_SOCK.connect((RHOST,RPORTS))
             print(f"Connection State: {RPORT}::Port Open")
             while True:
                 SND_DATA = "Secret"
                 C_SOCK.send(bytearray(SND_DATA,'utf8'))
                 RCV_DATA = C_SOCK.recv(1024)
                 print(RCV_DATA.decode())

             C_SOCK.close()
        except socket.error as e:
             print(f"Connection State: {RPORT}::Port Closed/Filtered")
             C_SOCK.close()


