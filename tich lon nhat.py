n=int(input())
a=list(sorted(list(map(int,input().split()))))
M=max(a[n-1]*a[n-2]*a[n-3],a[n-1]*a[0]*a[1],a[n-1]*a[n-2])
print(M)