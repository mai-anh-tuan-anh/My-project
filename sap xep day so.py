for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    max_element=max(a)
    a.insert(a.index(max_element),m)
    am,duong=[],[]
    for i in range(n+1):
        if(a[i]<0):
            am.append(a[i])
        else:
            duong.append(a[i])
    print(*am,*duong)