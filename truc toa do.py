for t in range(int(input())):
    n=int(input())
    a=[]
    while len(a)<n:
        a.append(list(map(int,input().split())))
    a=list(sorted(a,key=lambda x: (x[1],-x[0])))
    res=1
    cur=a[0][1]
    for i in range(1,len(a)):
        if(a[i][0]>=cur):
            res+=1
            cur=a[i][1]
    print(res)