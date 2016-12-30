def checkPrime(p):
    #print(p)
    if ((p==1) or (p%2==0)):
        print("Not prime")
        return

    for n in range(1,int((p-1)/2)+1):
        aux = (2*n+1)
        if (p%aux == 0) & (p!=aux) :
            print("Not prime p=",p,"aux=",aux)
            return
    print("Prime")
T = int(input().strip())
primes = []
for i in range(T):
    primes.append(int(input().strip()))

for p in primes:
    checkPrime(p)
