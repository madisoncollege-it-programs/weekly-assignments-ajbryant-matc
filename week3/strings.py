#!/usr/bin/env python3

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"'Hello {varName}'")
print(f"'{varRed}-{varGreen}-{varBlue}'")
print(f"'Is this {varGreen.lower()} or {varBlue.lower()}?'")
print(f"'My name is {varName.upper()}'")
print(f"'[{varRed:+^7s}]'")
print(f"'[{varGreen.lower():=<7s}]'")
print(f"'[{varBlue.lower():*>9s}]'")
print(f"'{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}'")
print(f"'{varLoot}'")
print(f"'{varLoot:<.1f}'")
print(f"'I have ${varLoot:<.2f}'")
print(f"'[{varRed:$^10s}] [{varGreen:$^10s}] [{varBlue:$^10s}]'")
print(f"'[{varRed[::-1]: ^10s}] [{varGreen: ^10}] [{varBlue[::-1]: ^10}]'")
print(f"'First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]'")
