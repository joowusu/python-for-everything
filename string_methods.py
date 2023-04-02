#!/usr/bin/env python3.7

"""
A python script that will allow a user to provide a string then
presents the user with some permutations (all lowercase, all uppercase, etc).
"""

message = input("Enter a message: ") # User imput.

# Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User Input.
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

# Separate the string and present the individual words as a list. 
words = message.split()  # Splits on a space by default. 
print("Words:", words)

# Sort list from above, then print the Alphabetic First and Last Words.
sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

