for t in range(int(input())):
    n,c,d=map(int,input().split())
    a=sorted(list(map(int,input().split())),reverse=True)
    Min=min(c,d)
    Max=max(c,d)
    sum1=sum(a[0:Min])/Min
    sum2=sum(a[Min:Min+Max])/Max
    print("{:.6f}".format(sum1+sum2))
