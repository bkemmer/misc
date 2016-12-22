import numpy as np
import statistics as stats
# import pdb; pdb.set_trace()
n = int(input().strip())
arr = [int(arr_tmp) for arr_tmp in input().strip().split(' ')]
a = np.array(arr)
print(int(np.percentile(a,25)))
print(int(np.percentile(a,50)))
print(int(np.percentile(a,75)))
