from collections import *
for t in range(int(input())):
    n=int(input())
    a=dict(Counter(list(map(int,input().split()))))
    for key,value in a.items():
        if value&1:
            print(key)
            break