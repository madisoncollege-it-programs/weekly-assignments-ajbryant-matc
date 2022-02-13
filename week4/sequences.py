#!/usr/bin/env python3

varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ]

print(f"'{varString[3::1]}'")
print(f"'{varString[:3:1]}'")
print(f"'{varString[3:12:1]}'")
print(f"'{varString[::2]}'")
print(f"'{varString[::-1]}'")

print(f"{varList[::-1]}")
print(f"{varList[-5::-1]}")
print(f"{varList[2:4]}")
print(f"{varList[::3]}")
print(f"{varList[1:]}")

for x in varString:
    print(f"This is X: {x}")

for x in varList:
    print(f"This is X: {x}")
