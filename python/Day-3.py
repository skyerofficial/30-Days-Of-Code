#!/bin/python3

import sys
N = int(input().strip())
# Condition Check
if N < 1 or N > 100:
    print("Weird")
else:
    if N%2:
        print("Weird")
    else:
        if N>0 and N<6:
            print("Not Weird")
        elif N<21:
            print("Weird")
        else:
            print("Not Weird")
