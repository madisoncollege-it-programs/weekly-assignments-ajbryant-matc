#!/usr/bin/env python3

#Author: Ashley Bryant
#Purpose: Import files and call functions from them.

from c2f import conTemp

from f2c import convertTemp


meas = input("Enter the unit of measurement: ('F' or 'C') ")

deg = input("Enter the temperature: ")
temp = int(deg)

if meas == 'F':
    print(f"{temp} degrees Fahrenheit equals {convertTemp(temp)} degrees Celsius") 

else:
    print(f'{temp} degrees Celsius equals {conTemp(temp)} degrees Fahrenheit')
