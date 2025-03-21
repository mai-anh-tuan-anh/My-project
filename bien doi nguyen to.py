from math import *
a=[1]*110000
a[0]=a[1]=0
nt=[]
def sang():
    for i in range(2,isqrt(110000)+1):
        if(a[i]):
            for j in range(i*i,110000,i):
                a[j]=0
    for i in range(2,110000):
        if(a[i]):
            nt.append(i)
if __name__=='__main__':
    n=int(input())
    sang()
    a=list(map(int,input().split()))
    res=0
    for i in a:
        cnt=10*9
        for j in nt:
            cnt=min(cnt,abs(i-j))
        res=max(res,cnt)
    print(res)