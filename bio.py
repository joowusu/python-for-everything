# Prompt user for input
name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

# Prints user information on three different lines.
# By default the print function adds a new line.
print(name)
print("is " + str(age) + " years old")
print("and loves the color " + color + ".")

# Prints user information on one line
print(name + " is " + str(age) + " years old and loves the color " + color + ".")

# end parameter " " ends the output with a space
print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".")

# sep parameter add a space after a commma.
print(name, 'is', age, 'years old and loves the color', color + ".", sep=" ")
