n=int(input())
matrix=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
k=int(input())
nuatren,nuaduoi=0,0
for i in range(n):
    for j in range(n):
        if(i<n-j-1): nuatren+=matrix[i][j]
        elif(i>n-j-1):nuaduoi+=matrix[i][j]
dochenhlenh=abs(nuatren-nuaduoi)
print('YES' if(dochenhlenh<=k) else 'NO')
print(dochenhlenh)