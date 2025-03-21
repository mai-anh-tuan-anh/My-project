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
        st=set()
        while Prime[idx]<n:
            num=str(Prime[idx])
            if(num in st or num[::-1] in st): 
                idx+=1 
                continue
            if(num!=num[::-1]):
                if isPrime[int(num[::-1])] and int(num[::-1])<n: 
                    print(num,num[::-1],end=' ') 
                    st.add(num)
                    st.add(num[::-1])
            idx+=1
        print()