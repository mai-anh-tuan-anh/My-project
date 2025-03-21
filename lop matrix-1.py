for t in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    chuyenvi=[]
    for i in range(m):
        temp=[0]*n
        for j in range(n):
            temp[j]=a[j][i]
        chuyenvi.append(temp)
    res=[]
    for i in range(n):
        temp=[0]*n
        res.append(temp)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j]+=a[i][k]*chuyenvi[k][j]
    for i in range(n):
        print(*res[i])