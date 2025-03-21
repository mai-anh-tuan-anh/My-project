from itertools import *
for t in range(int(input())):
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    b=list(permutations(a))
    print(len(b))
    for i in range(len(b)-1,-1,-1):
        for num in b[i]:
            print(num,end='')
        print(end=' ')
    print()