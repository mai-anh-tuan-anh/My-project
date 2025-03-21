from collections import *
x=input()
k=int(input())
st=set()
dt=defaultdict()
while len(x)>0:
    num=x[:2]
    if len(num)==2:
        if num not in dt:
            dt[num]=1
        else:
            dt[num]+=1
    x=x[2:]
ok=True
dt=sorted(dt.items(),key= lambda x:(x[0]))
for item in dt:
    if(item[1]>=k):
        ok=False
        print(*item)
if ok:
    print('NOT FOUND')