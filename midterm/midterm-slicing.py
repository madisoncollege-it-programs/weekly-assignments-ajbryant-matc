#!/usr/bin/env python3
#Author:
print("Name: Ashley Bryant")

#Purpose: Extract words and strings from a file and join them into a phrase.

with open('slicing-file.txt', 'r') as hfile:
    varList = hfile.readlines()
print(f'{varList[24:25:]}')
print(f'{varList[2:5:]}')
print(f'{varList[17:12:-2]}')
print(f'{varList[10:13:]}')
print(f'{varList[8:5:-1]}')

quote =' '.join(['Whether', 'you', 'think', 'you', 'can', 'or', 'think', 'you', 'can\'t,', 'you', 'are', 'right'])
print(quote)
