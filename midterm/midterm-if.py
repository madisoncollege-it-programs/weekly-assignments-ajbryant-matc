#!/usr/bin/env python3

#Author:
print("Ashley Bryant")

#Purpose: To demonstrate pulling data out of a list, converting it to intergers, and adding up a total. 

line_number = 0
Total = 0



with open('Midterm-if.txt', 'r') as myFile:
    for line in myFile:
        if 'gmeach18@ed.gov' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        if '248.253.63.149' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        if 'Whiteland' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        if '80.222.19.190' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        if 'Kayley' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        if 'dcassyqw@microsoft.com' in line:
            Total = (int(line_number) + Total)
            print(f'{line_number}')
        line_number += 1

print(f'The total is: {Total}')
