#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_rev = []
for i in range(len(arr)-1,-1,-1):
    arr_rev.append(str(arr[i]))
print(' '.join(arr_rev))
