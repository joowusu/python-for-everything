#/usr/bin/env  python3.6

"""
A python script that prompts a user to enter an integer and:
a.  prints "Fizz" if the integer is a multple of 3.
b.  prints "Buzz" if the integer is a multple of 5.
c.  prints "FizzBuzz" if the integer is a multiple of 3 and 5.
"""

number = int(input("Enter an integer value: "))

# The % operator is the modulo, which returns the remainder rather than the quotient after division.
if number % 3 == 0 and number % 5 == 0:
     print("FizzBuzz")

elif number % 3 == 0:
     print("Fizz")

elif number % 5 == 0:
     print("Buzz")

else:
    print(number, "is not a multiple of \"3 or 5\", OR \"3 and 5.\"")
