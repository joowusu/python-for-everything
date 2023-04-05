"""
A python scripts that prompts a user for a integer number "n", 
and prints the square of numbers less than n, i.e (i < n)^2. 
Contraints:  "n" should be between 1 and 20 (inclusive).

By Joan Owusu
"""
#!/usr/bin/env python3.7

if __name__ == '__main__':
        
    n = int(input("Enter an integer number: ")) # prompts user for an integer number.
    print()
    x = [*range(n)] # Integer numbers less than "n"
    print()
    
    if n >= 1 and n <= 20:  # n is a non-negative integer between 1 and 20 (inclusive).
        print("List of non-negative integers that are less than", n, ": ", x)
        print()
        
        for i in x:
            print(i, "squared is: ",  i**2)
            #print(pow(i,2)) # the power method can also be used, pow(base, exp).
                
    elif n <= 0:  # n is 0 or a non-negative integer.
        print("Integer number cannot be 0 or negative.  Goodbye!!!")
        
    else:
        print("Integer number cannot be greater than 20.  Goodbye!!!")
        
print()