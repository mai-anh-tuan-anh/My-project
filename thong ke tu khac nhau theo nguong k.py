import re
n,k=map(int,input().split())
a = {}
for i in range(n):
    for s in re.split("[^a-z0-9]", input().lower()):
        if s != '':
            if s not in a: a[s]=1
            else: a[s]+=1
ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: 
    if a[i]>=k:
        print(i,a[i])