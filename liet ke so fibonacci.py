F=[0]*1000
F[0]=0
F[1]=F[2]=1
for i in range(3,100):
    F[i]=F[i-1]+F[i-2]
for t in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    for i in range(a,b+1):
        print(F[i],end=' ')
    print()