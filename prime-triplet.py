from math import *
isPrime=[1]*1000005
Prime=[]
isPrime[0]=isPrime[1]=0
for i in range(2,1000):
    if(isPrime[i]):
        for j in range(i*i,1000005,i):
            isPrime[j]=0
for i in range(2,10**6+5):
    if(isPrime[i]):
        Prime.append(i)
if __name__=='__main__':
    for t in range(int(input())):
        n=int(input())
        idx=0
        cnt=0
        while Prime[idx]<=n-6:
            num=Prime[idx]
            if isPrime[num+6]==1 and (isPrime[num+4]==1 or isPrime[num+2]==1):
                cnt+=1
            idx+=1
        print(cnt)