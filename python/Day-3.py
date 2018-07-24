#!/bin/python3
# SheBang! for Python 3
import sys
N = int(input().strip())
# Define the range for the number
if N < 1 or N > 100:
    print("Weird")
else:
    # Check for Odd / Even 
    if N%2:
        print("Weird")
    else:
        if N>0 and N<6:
            print("Not Weird")
        elif N<21:
            print("Weird")
        else:
            print("Not Weird")
