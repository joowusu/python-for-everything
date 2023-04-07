#!/usr/bin/env python3.7

"""
A python script that generators a list of numbers  
in the range of 1 to 100 using a using a foor loop.
"""

import random  # importing the random module.

randomlist = [] # creates an empty list.

number = int(input("Enter list size. Example 5, 10, 15, etc. numbers in the list: ")) # prompts user for an number.
print()

for i in range(0, number): # list will contain 5 numbers. 
    random_number = random.randint(1, 100) # The randint() method generates a integer between a given range of numbers.S
    randomlist.append(random_number) # append randon number to the empty list "randomlist."

print("Random numbers generated between 1 and 100:", randomlist) 
print()

