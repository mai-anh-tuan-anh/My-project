from math import *
from collections import *
def nguyento(n):
    if n<=1: return False
    if n<=3: return True
    if (n%2==0) or (n%3==0): return False
    for i in range(5,isqrt(n)+1,6):
        if (n%i==0) or (n%(i+2)==0):
            return False
    return True
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    for i in b:
        if(nguyento(i)):
            print(i,b[i])