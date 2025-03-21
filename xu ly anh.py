import sys
def read_ints():
    return map(int, sys.stdin.readline().split())
def solve():
    T = int(sys.stdin.readline())
    results = []
    for _ in range(T):
        n, m, l = read_ints()
        k = l // 2
        a = [list(read_ints()) for _ in range(n)]
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix[i+1][j+1] = (prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + a[i][j])
        res = []
        for i in range(k, n - k):
            row = []
            for j in range(k, m - k):
                total = (
                    prefix[i+k+1][j+k+1] 
                    - prefix[i-k][j+k+1] 
                    - prefix[i+k+1][j-k] 
                    + prefix[i-k][j-k]
                )
                row.append(str(total // (l * l)))
            res.append(" ".join(row))
        results.append("\n".join(res))
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    solve()
        