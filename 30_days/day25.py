def checkPrime(p):
    odds = []
    odds.append(2)
    for n in range(1,int((p-1)/2)+1):
        odds.append(2*n+1)
    try:
        odds.remove(p)
    except:
        pass
    #print(odds)
    if(p==1):
        print("Not prime")
        return
    for o in odds:
        if p%o == 0 :
            print("Not prime")
            return
    print("Prime")
T = int(input().strip())
primes = []
for i in range(T):
    primes.append(int(input().strip()))

for p in primes:
    checkPrime(p)
