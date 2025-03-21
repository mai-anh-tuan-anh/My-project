from math import *
x1,y1,x2,y2=map(int,input().split())
tu=x1*y2+x2*y1
mau=y1*y2
uoc=gcd(tu,mau)
print(tu//uoc,'/',mau//uoc,sep='')