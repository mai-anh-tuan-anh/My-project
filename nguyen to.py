from math import isqrt,gcd
t=int(input())
while t>0:
    t-=1
    n=int(input())
    k=n
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            while n%i==0:
                n//=i
            k-=k//i
    if n>1:
        k-=k//n
    ok=True
    if(k<2):
        print('NO')
        continue
    for i in range(2,isqrt(k)+1):
        if(k%i==0):
            ok=False
            print('NO')
            break
    if ok:
        print('YES')    

