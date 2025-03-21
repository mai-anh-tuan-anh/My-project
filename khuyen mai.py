n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in range(n):
    res.append([a[i],b[i],a[i]-b[i]])
res=sorted(res,key=lambda x:(x[2]))
sum=0
cnt=0
for i in range(n):
    if(cnt<k):
        sum+=res[i][0]
        cnt+=1
    else:
        if(res[i][2]>=0):
            sum+=res[i][1]
        else:
            sum+=res[i][0]
print(sum)