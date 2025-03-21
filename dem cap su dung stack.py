import sys
import bisect
from collections import deque
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:n+1]))
sorted_unique = sorted(set(a))
index_map = {val: idx for idx, val in enumerate(sorted_unique)}
a = [index_map[val] for val in a]
m = [[] for _ in range(len(sorted_unique))]
for i in range(n):
    m[a[i]].append(i)
def get_nearest(arr, start, end, step, root):
    st = deque()
    for i in range(start, end, step):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        arr[i] = root if not st else st[-1]
        st.append(i)
l, r = [-1] * n, [n] * n
get_nearest(l, 0, n, 1, -1)
get_nearest(r, n - 1, -1, -1, n)
def count_in_range(arr, start, end):
    if start >= len(arr) or end < arr[start]: return 0
    pos = bisect.bisect_right(arr, end) - 1
    return pos - start + 1 if pos >= start else 0
s = 0
first = [0] * len(sorted_unique)
for i in range(n):
    if l[i] != -1:
        s += 1
    if r[i] != n:
        s += 1
    x = count_in_range(m[a[i]], first[a[i]], r[i] - 1)
    s += (x - 1) * x // 2
    first[a[i]] += x
print(s)