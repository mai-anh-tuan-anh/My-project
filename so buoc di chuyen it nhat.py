import sys
from collections import deque
def test_case():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = [[float('inf')] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    res[0][0] = 0
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:
            print(res[r][c])
            return
        if r + 1 < n:
            i, j = r + abs(a[r][c] - a[r + 1][c]), c
            if i < n and res[i][j] == float('inf'):
                res[i][j] = res[r][c] + 1
                q.append((i, j))
        if c + 1 < m:
            i, j = r, c + abs(a[r][c] - a[r][c + 1])
            if j < m and res[i][j] == float('inf'):
                res[i][j] = res[r][c] + 1
                q.append((i, j))
        if r + 1 < n and c + 1 < m:
            i = r + abs(a[r][c] - a[r + 1][c + 1])
            j = c + abs(a[r][c] - a[r + 1][c + 1])
            if i < n and j < m and res[i][j] == float('inf'):
                res[i][j] = res[r][c] + 1
                q.append((i, j))
    print(-1)
def main():
    sys.stdin = open(0) 
    t = int(input())
    for _ in range(t):
        test_case()
        print()
if __name__ == "__main__":
    main()
