import sys
N = int(input().strip())
if (N%2 > 0): print("Weird")
elif N>20: print("Not Weird")
elif N>=6: print("Weird")
else: print("Not Weird")