n=int(input())
a=[]
while len(a)<n:
    a.extend(list(map(int,input().split())))
chan,le=[],[]
for i in a:
    if i&1:
        le.append(i)
    else:
        chan.append(i)
le=sorted(le,reverse=True)
chan=sorted(chan)
i,j=0,0
for k in a:
    if k&1:
        print(le[i],end=' ')
        i+=1
    else:
        print(chan[j],end=' ')
        j+=1

