#!/bin/python3

import sys
N = int(input().strip())
multiple = 1
# Computaions
if N >=2 and N <=20:
    for i in range(1,11):
        multiple = i*N
        print("%s x %s = %s" % (N,i,multiple))
