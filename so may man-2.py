t=int(input())
while t>0:
    t-=1
    n=int(input())
    ok=True
    while(n>0):
        if(n%10!=4 and n%10!=7):
            print('NO')
            ok=False
            break
        n//=10
    if ok:
        print('YES')