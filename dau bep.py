from sys import stdin
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = [0] + sorted(map(int, stdin.readline().split()))
    #dp[i][j] minimum of cake 1 -> i when cooking end at j
    dp = [[0] * (300) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, 300):
            if a[i] >= i and j>a[i]: dp[i][j] = min(dp[i-1][a[i] - 1], dp[i-1][j-1] + abs(a[i] - j))
            else: dp[i][j] = dp[i-1][j-1] + abs(a[i] - j)
    print(min(dp[n][n:]))