import math
def checkPrime(p):
    if p==1:
        print("Not prime")
        return
    is_prime = True
    for j in range(2, int(math.sqrt(p)+1)):
        if p % j == 0:
            is_prime = False
            # print("Not prime p=",p,"j=",j)
            print("Not prime")
            return
    if is_prime:
        # print("Prime p=",p)
        print("Prime")

T = int(input().strip())
primes = []
for i in range(T):
    primes.append(int(input().strip()))

for p in primes:
    checkPrime(p)
