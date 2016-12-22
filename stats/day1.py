import statistics as stats
# import pdb; pdb.set_trace()
n = int(input().strip())
arr = [int(arr_tmp) for arr_tmp in input().strip().split(' ')]
arr.sort()
# print(arr[:4])
if n%2 > 0 :
    q1 = stats.median(arr[:int(n/2)])
    q3 = stats.median(arr[int(n/2)+1:])
else:
    q1 = stats.median(arr[:int(n/2)])
    q3 = stats.median(arr[int(n/2):])
q2 = stats.median(arr)
print(int(q1))
print(int(q2))
print(int(q3))
