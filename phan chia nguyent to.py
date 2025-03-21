from math import *
def nt(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,isqrt(n)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
if __name__=='__main__':
    n=int(input())
    a=list((map(int,input().split())))
    b=[]
    st=set()
    sum=0
    for i in a:
        if i not in st:
            b.append(i)
            sum+=i
            st.add(i)
    prefix=[0]*(len(b)+1)
    for i in range(1,len(b)+1):
        prefix[i]=prefix[i-1]+b[i-1]
    lt=-1
    for i in range(1,len(b)+1):
        total=prefix[i]-prefix[0]
        if(nt(total) and nt(sum-total)):
            lt=i-1
            break
    print('NOT FOUND' if lt==-1 else lt)
