n=int(input())
a=list(map(int,input().split()))
res,sobuoc=0,10**9
for i in range(n):
    cnt=0
    for j in range(n):
        if i!=j:
            cnt+=abs(a[i]-a[j])
    if(cnt<sobuoc):
        res=a[i]
        sobuoc=cnt
print(sobuoc,res)