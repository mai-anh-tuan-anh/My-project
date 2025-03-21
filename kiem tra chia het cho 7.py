for t in range(int(input())):
    n=input()
    ok=True
    for i in range(1000):
        if(int(n)%7==0):
            print(n)
            ok=False
            break
        n=str(int(n)+int(n[::-1]))
    if ok:
        print('-1')

