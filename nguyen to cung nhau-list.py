from math import *
n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
for i in (range(n-1)):
    for j in range(i+1,n):
        if(gcd(a[i],a[j])==1):
            print(a[i],a[j])
