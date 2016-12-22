class nonNegatives(Exception):
    def __init__(self, message):
        pass

class Calculator(object):
    def power(self,n,p):
        if (n<0 or p <0):
            raise nonNegatives('n and p should be non-negative'.format(Exception))
        return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int,input().split())
    try:
        ans = myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
