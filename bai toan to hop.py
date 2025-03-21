from itertools import combinations
n,k=input().split()
comb = combinations(sorted(set(input().split()),key=int),int(k))
for lst in comb:
    for item in lst:
        print(item,end=' ')
    print()