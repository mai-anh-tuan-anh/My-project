from math import *
a=[1]*(10**6+1)
a[0]=a[1]=0
nt=[]
def sang():
    for i in range(2,isqrt(10**6)+1):
        if a[i]:
            for j in range(i*i,10**6+1,i):
                a[j]=0
if __name__=='__main__':
    sang()
    for i in range(2,10**6+1):
        if a[i]:
            nt.append(i)
    n=int(input())
    cnt=0
    for p in nt:
        if p**8 > n: break
        cnt+=1
    for i in range(len(nt)):
        if nt[i]**4>n: break
        for j in range(i+1,len(nt)):
            if (nt[i]**2) * (nt[j]**2) > n: break
            cnt+=1
    print(cnt)