for t in range(int(input())):
    n=int(input())
    a=[]
    while(len(a)<n):
        a.append(list(map(float,input().split())))
    M=1
    dp=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if a[i][0]>a[j][0] and a[i][1]<a[j][1]:
                dp[i]=max(dp[i],dp[j]+1)
                M=max(M,dp[i])
    print(M)