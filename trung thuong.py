from collections import *
for t in range(int(input())):
    n=int(input())
    dt=defaultdict(int)
    for item in range(n):
        dt[int(input())]+=1
    dt=sorted(dt.items(),key=lambda x:(x[1],-x[0]))
    print(dt[-1][0])