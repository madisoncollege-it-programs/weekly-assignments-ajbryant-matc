#!/usr/bin/env python3
#Author:
print("Name: Ashley Bryant")

#Purpose: Extract words and strings from a file and join them into a phrase.

with open('slicing-file.txt', 'r') as hfile:
    varList = hfile.readlines()
myList = ((f'{varList[24:25:]} '),(f'{varList[2:5:]} '),(f'{varList[17:12:-2]} '),(f'{varList[10:13:]} '),(f'{varList[8:5:-1]}'))

myString = ''.join(myList)

quote = str(myString).replace('[','').replace(']','').replace(',','').replace('\n','').replace("'",'')
print(quote)
