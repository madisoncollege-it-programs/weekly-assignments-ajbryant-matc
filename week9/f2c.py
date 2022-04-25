#!/usr/bin/env python3

#Author: Ashley Bryant
#Purpose: Create a function to convert Fahrenheit to Celsius


def convertTemp(f):
    #find temperature in Celsius
    c = (f - 32) * (5/9)
    return c

if __name__ == "__main__":

    fahr = float(input("Enter degrees in Fahrenheit: "))

    cel = convertTemp(fahr)

    print(f"{fahr} degrees Fahrenheit is equal to {cel} degrees Celsius")
