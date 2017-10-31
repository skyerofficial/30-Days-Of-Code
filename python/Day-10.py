#!/bin/python3

import sys
# get the input number
n = int(input().strip())
def max(a,b):
    return a if a>b else b
maxN = 0
count = 0
while n:
    while n&1:
        count+=1
        n>>=1
    maxN = max(count,maxN)
    if not n&1:
        count = 0
        n>>=1
print(maxN)
    
