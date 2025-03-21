n=int(input())
a=list(map(int,input().split()))
a=sorted(a,key=int)
for i in a:
    if(i+1) not in a:
        print(i+1)
        break