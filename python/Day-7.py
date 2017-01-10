#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
string = ""
for i in range(n-1,-1,-1):
    string += (str(arr[i])+" ")
print(string)
