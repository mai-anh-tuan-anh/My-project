def tichchuso(n):
    tich=1
    while n>0:
        tich*=n%10
        n//=10
    return tich
if __name__=='__main__':
    for t in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        a=sorted(a,key=lambda x: (tichchuso(x),x))
        for i in a:
            print(i,end=' ')
        print()