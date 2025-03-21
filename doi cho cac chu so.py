def find_max_smaller_number(s):
    n = len(s)
    s = list(s)
    i = n - 2
    while i >= 0 and s[i] <= s[i + 1]:
        i -= 1
    if i == -1:
        return "-1"
    max_j = i + 1
    for j in range(i + 1, n):
        if s[j] < s[i] and s[j] > s[max_j]:
            max_j = j
    s[i], s[max_j] = s[max_j], s[i]
    if s[0] == '0':
        return "-1"
    return "".join(s)
T = int(input())
for _ in range(T):
    s = input().strip()
    print(find_max_smaller_number(s))