from itertools import *
n, k = map(int,input().split())
s = sorted(set(input().split())) 
for i in combinations(s, k): 
    print(*i)