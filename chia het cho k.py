a,K,N=map(int,input().split())
b=K-a%K
check=1
for i in range(a+b,N+1,K):
    check=0
    print(i-a,end=' ')
if check:
    print('-1')