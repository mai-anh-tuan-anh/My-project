from collections import *
x=input()
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
for key,value in dt.items():
    print(key,value)