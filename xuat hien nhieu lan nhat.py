from collections import *
for t in range(int(input())):
    n=int(input())
    dt=defaultdict(int)
    lst=list(map(int,input().split()))
    for i in range(n):
        dt[lst[i]]+=1
    dt=sorted(dt.items(), key=lambda x:(x[1],-x[0]))
    if(dt[-1][1]>n//2):
        print(dt[-1][0])
    else:
        print('NO')

