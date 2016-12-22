#!/bin/python3gi
#bubble sort
import sys
#import pdb; pdb.set_trace()

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numberSwaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numberSwaps += 1

print("Array is sorted in %d swaps." % numberSwaps)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[len(a)-1])
