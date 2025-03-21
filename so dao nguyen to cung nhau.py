from math import *
for t in range(int(input())):
    n=input()
    rev_n=n[::-1]
    n=int(n)
    rev_n=int(rev_n)
    if(gcd(n,rev_n)==1):
        print('YES')
    else:
        print('NO')