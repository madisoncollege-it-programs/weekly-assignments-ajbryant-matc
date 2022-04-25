#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Use argparse to set up help options.

import argparse

print(f'This is Ashley Bryant\'s script')

parser = argparse.ArgumentParser(description = 'Argparse Lab')


parser.add_argument('-m BASIC', help='Enter some text')
parser.add_argument('-i', '--an integer', dest='varInteger', type=int, default=10, required=True, help='Enter a simple integer')
parser.add_argument('-d', '--a float', dest='varFloat', metavar='[a float]', default=10.0, type=float, help='Enter a simple float')
parser.add_argument('-s', '--a string', dest='varString', type=str, default='Hello', help='Enter a simple string')
parser.add_argument('-l', '--strings', dest='varList', metavar = '[strings] ...', nargs='+', help='Enter a list of strings (space delimited)' )
parser.add_argument('-t', '--set-true', dest='varBool_t', action='store_true', help='Toggle from default false to true')
parser.add_argument('-f', '--setfalse', dest='varBool_f', action='store_false', help='Toggle from default true to false')
parser.add_argument('-v', '--version', action='version', version='%9prog0s 2.0', help='show program\'s version number and exit')


args = parser.parse_args()

print(args)
print(type(args.varInteger),args.varInteger)
print(type(args.varString),args.varString)
print(type(args.varFloat),args.varFloat)
print(type(args.varList),args.varList)
