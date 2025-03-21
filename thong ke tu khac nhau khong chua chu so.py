import re
a = {}
for i in range(int(input())):
    for s in re.split("[^a-z]", input().lower()):
        if s != '':
            if s not in a: a[s]=1
            else: a[s]+=1
ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: 
    try:
        i=int(i)
    except:
        print(i, a[i])