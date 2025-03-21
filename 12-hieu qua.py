a0,b0,c0=map(int,input().split())
a1,b1,c1=map(int,input().split())
ok=True
if(a1<a0): a1+=24
elif(a1==a0):
    if(b1<b0):a1+=24
    elif(b1==b0):
        if(c1<c0):a1+=24
        elif(c1==c0): 
            print(0)
            ok=False
if ok:
    start=a0*3600+b0*60+c0
    end=a1*3600+b1*60+c1
    print(end-start)