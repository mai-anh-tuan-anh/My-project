for t in range(int(input())):
    n=int(input())
    x,y,z=map(int,input().split())
    dp=[10**5]*(n+1)
    dp[0],dp[1]=0,x
    for i in range(2,n+1):
        dp[i]=min(dp[i],dp[i-1]+x)
        if i&1:
            dp[i]=min(dp[i],dp[i//2]+x+z,dp[i//2+1]+y+z)
        else:
            dp[i]=min(dp[i],dp[i//2]+z,dp[i//2+1]+y+z)
    print(dp[n])