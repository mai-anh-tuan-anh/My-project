for t in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    a=a[d:]+a[:d]
    print(*a)