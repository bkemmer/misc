n = int(input().strip())

for i in range(n):
    s = str(input().strip())
    even = []
    odd = []
    for k in range(0,len(s)):
        if(k%2 >0):
            odd.append(s[k])
        else:
            even.append(s[k])
    even_str = ''.join(str(e) for e in even)
    odd_str = ''.join(str(o) for o in odd)
    print(even_str," ",odd_str, sep='')
