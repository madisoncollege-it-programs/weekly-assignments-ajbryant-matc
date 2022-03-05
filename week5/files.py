#!/usr/bin/env python3

# Author: Ashley Bryant
# Purpose: The script will demonstrate various ways to view and manipulate files.


myfile = open('/etc/passwd', 'r')
filestring = myfile.read()
print(f"The read function is commonly used when the file contents are a string.")
print(filestring)
print(type(filestring))
print(f"The length function here counts the number of characters in a string.")
print(len(filestring))
myfile.close()

myfile = open('/etc/passwd', 'r')
filestring = myfile.readlines()
print(f"The readlines function is used when you want to read the entire file and store it as a list.")
print(filestring)
print(type(filestring))
print(f"The length function in this case counts the number of items in the list.")
print(len(filestring))
myfile.close()

myfile = open('/etc/passwd', 'r')
listfiletext = myfile.readline()
print(f"The readline function is used when you would like to read the file one line at a time.")
print(listfiletext)
filestring = myfile.read()
print(len(filestring))
print(type(listfiletext))
myfile.close()
