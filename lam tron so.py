t=int(input())
while t>0:
    t-=1
    lst=list(map(int,input()))
    for i in range(len(lst)-1,-1,-1):
        if lst[i]>=5 and i!=0:
            lst[i-1]+=1
        if(i!=0): lst[i]=0
    for i in range(0,len(lst)):
        print(lst[i],end='')
    print()
