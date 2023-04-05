
#!/usr/bin/env python3.7

"""
A python script that prompts the user for an integer (contraints: 1 <= n <= 100), 
and prints the following conditional actions:

a.  If the integer is odd, print "Weird."
b.  If the integer is even and in the inclusive range of 2 to 5, print "Not Weird."
c.  If the integer is even and in the inclusive range of 6 to 20, print "Weird."
d.  If the integer is even and greater than , print "Not Weird."
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    n = int(input().strip())
    range_1 = range(2, 6)  # inclusive range of 2 to 5.
    range_2 = range(6, 21) # inclusive range or 6 to 20.
    
if n >= 1 and n <= 100:    
    
    if n % 2 != 0:
        print("Weird")
        
    elif n % 2 == 0 and n in range_1:
        print("Not Weird")
        
    elif n % 2 == 0 and n in range_2:
        print("Weird")
        
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
else:
    exit()
