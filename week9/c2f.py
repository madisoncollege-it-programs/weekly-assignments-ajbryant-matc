#!/usr/bin/env python3

#Author: Ashley Bryant
#Purpose: Create a function to convert Celsius to Fahrenheit

def conTemp(c):
    #find temperature in fahrenheit
    f = (c * 1.8) + 32
    return f

if __name__ == "__main__":

    cel = float(input("Enter degrees in Celsius: "))

    fahr = conTemp(cel)

    print(f"{cel} degrees Celsius is equal to {fahr} degrees Fahrenheit")
