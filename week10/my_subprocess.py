#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Extract system processes, list them, and count them.

import subprocess

myProc = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode()
myProcList = myProcString.split('\n')

for item in myProcList:
    print(item)

print(len(myProcList[1::]))
