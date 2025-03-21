while True:
    x=int(input())
    if x==-1: break
    while x%9!=0:
        x+=1
    print(x)