#!/usr/bin/env python3

# Author: Ashley Bryant
# Purpose: This script will

print("""You enter a dark room with three doors. 
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

# == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")

# == Door Number 3 Logic ====================
elif door == "3":
    print("You are met with 2 more doors holding either 1,000,000 or your heart's greatest desire.\n")

    print("1. Give me that money!")
    print("2. My heart's desire is such a mystery, surprise me!")

# == Greedy Logic ====================
    Greedy = input("-> ")

    if Greedy == "1":
        print("1) Congratulations on your 1,000,000 Indonesian Rupiah, here's your $69.49 US dollars! Good job! Walking down the street you get robbed.")
    elif Greedy == "2":
        print("2) Congratulations, your heart's desire at 5 years old was a 1969 Chevelle Hot Wheels. Good job! Your child sticks it in the garbage disposal.")
else:
    print("You did not select a door??? Good Call :)")
