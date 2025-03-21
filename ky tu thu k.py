def find_kth_character(n, k):
    length = (1 << n) - 1
    if k == (length // 2) + 1:
        return chr(64 + n)
    elif k <= length // 2:
        return find_kth_character(n - 1, k)
    else:
        return find_kth_character(n - 1, k - (length // 2) - 1)
for t in range(int(input())):
    N, K = map(int, input().split())
    print(find_kth_character(N, K))