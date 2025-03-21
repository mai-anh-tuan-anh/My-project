t=int(input())
while t>0:
    t-=1
    n,x,m=map(float,input().split())
    cnt=0
    while n<m:
        n+=x*n/100
        cnt+=1
    print(cnt)
