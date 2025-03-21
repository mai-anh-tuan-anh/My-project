from math import *
def nguyento(n):
    if n<=1: return False
    if n<=3: return True
    if (n%2==0) or (n%3==0): return False
    for i in range(5,isqrt(n)+1,6):
        if (n%i==0) or (n%(i+2)==0):
            return False
    return True
if __name__=='__main__':
    n,m=map(int,input().split())
    for i in range(n):
        a=list(map(int,input().split()))
        for item in a:
            print('1' if nguyento(item) else '0',end=' ')
        print()