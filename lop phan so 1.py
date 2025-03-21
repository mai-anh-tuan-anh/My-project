from math import *
tu,mau=map(int,input().split())
num=gcd(tu,mau)
print(tu//num,'/',mau//num,sep='')