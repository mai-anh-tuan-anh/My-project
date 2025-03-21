from math import *
from functools import *
inf = 10**9
def min_cost_to_reach_all(n, a, c):
    pairs = sorted(zip(a, c))
    if reduce(gcd, a) != 1:
        return -1
    dp = {0: 0}
    for ai, ci in pairs:
        new_dp = dp.copy()
        for g, cost in dp.items():
            new_gcd = gcd(g, ai)
            new_dp[new_gcd] = min(new_dp.get(new_gcd, inf), cost + ci)
        dp = new_dp
    return dp[1] if 1 in dp else -1
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(min_cost_to_reach_all(n, a, c))