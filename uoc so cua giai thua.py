def cnt(n, p):
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count
T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    print(cnt(N, P))