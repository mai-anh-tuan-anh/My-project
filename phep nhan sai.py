while True:
    a=input().split()
    if int(a[0])==-1: break
    y,z=a[0],a[1]
    cnt=0
    if(int(z)==0):
        if(int(y)==0): continue
        print(cnt)
        continue
    elif(int(y)==0):
        continue
    for i in y:
        cnt+=int(i)
    print(int(z)//cnt)