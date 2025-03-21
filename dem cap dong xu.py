from math import *
n=int(input())
a=[]
for i in range(n):
    a.append(input())
row,col=[0]*n,[0]*n
for i in range(n):
    for j in range(n):
        if a[i][j]=='C':
            row[i]+=1
            col[j]+=1
cnt=0
for i in row:
    if i>=2:
        cnt+=comb(i,2)
for i in col:
    if i>=2:
        cnt+=comb(i,2)
print(cnt)