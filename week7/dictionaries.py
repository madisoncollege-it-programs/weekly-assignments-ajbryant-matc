#!/usr/bin/env python3

# Author: Ashley Bryant
# Purpose:This lab will demostrate creating dictionaries in python.


mydict = dict ()

mydict = {'server1.testlab.com':'192.168.1.10', 'server2.testlab.com':'192.168.1.11', 'server3.testlab.com':'192.168.1.12', 'server4.testlab.com':'192.168.1.13', 'server5.testlab.com':'192.168.1.14', 'server6.testlab.com':'192.168.1.15', 'server7.testlab.com':'192.168.1.16', 'server8.testlab.com':'192.168.1.17' }

print(mydict.keys())

print(mydict.values())

print(mydict.items())


if 'server2.testlab.com' in mydict:
    print('Yes')
else:
    print('No')

if 'server10.testlab.com' in mydict:
    print('Yes')
else:
    print('No')

