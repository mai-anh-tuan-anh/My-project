from math import *
def nguyento(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,isqrt(n)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def check(a,b):
    n=gcd(a,b)
    tong=0
    while n>0:
        tong+=n%10
        n//=10
    if nguyento(tong):
        return True
    else:
        return False
if __name__=='__main__':
    for t in range(int(input())):
        a,b=map(int,input().split())
        if check(a,b):
            print('YES')
        else:
            print('NO')