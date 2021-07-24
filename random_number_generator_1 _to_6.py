#!/usr/bin/env python3

print("Random Number Generator from 1 to 6")
print()

import random

random_number = random.randint(1, 6)
print("Nahodne cislo: ", random_number)

a = 4
while a == 4:
    
    again = input("again?")

    if again == "yes": 
        nahodne_cislo = random.randint(1,6)
        print("Nahodne cislo: ", random_number)

    if again == "no": 
        break

print()
print()
print("made by Jachym Tomasek, python@tomasek.tech, www.tomasek.tech")
input()
