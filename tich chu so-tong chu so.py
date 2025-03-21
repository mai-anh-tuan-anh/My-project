def check(n):
    lst=list(n)
    tong=0
    tich=0
    for i in range(len(lst)):
        if not i%2 and int(lst[i])!=0:
            if tich==0:
                tich=int(lst[i])
            else:
                tich*=int(lst[i])
        elif i%2:
            tong+=int(lst[i])
    print(tich,tong)
if __name__=='__main__':
    for t in range(int(input())):
        check(input())