from math import *
nguyento=[1]*100000
nguyento[0]=nguyento[1]=0
def sang():
    for i in range(2,isqrt(100000)+1):
        if(nguyento[i]):
            for j in range(i**2,100000,i):
                nguyento[j]=0
if __name__=='__main__':
    n,x=map(int,input().split())
    sang()
    so=[]
    for i in range(2,100000):
        if(nguyento[i]):
            so.append(i)
    i=0
    while n+1>0:
        print(x,end=' ')
        x+=so[i]
        i+=1
        n-=1