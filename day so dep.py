for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(n-1):
        Min=min(a[i],a[i+1])
        Max=max(a[i],a[i+1])
        while(Min*2<Max):
            Min*=2
            cnt+=1
    print(cnt)