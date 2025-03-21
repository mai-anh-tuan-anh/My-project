n=int(input())
b=[]
for t in range(n):
    b.append(list(map(int,input().split())))
a=[0]*n
if n==2:
    print(b[0][1]//2,b[0][1]//2)
else:
    a[1]=(b[0][1]-b[0][2]+b[1][2])//2
    a[0]=b[0][1]-a[1]
    for i in range(2,n):
        a[i]=b[0][i]-a[0]
    print(*a)