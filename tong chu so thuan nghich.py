def check(n):
    tong=0
    while n>0:
        tong+=n%10
        n//=10
    tong=str(tong)
    if(len(tong)==1): return False
    return tong==tong[::-1]
if __name__=='__main__':
    for t in range(int(input())):
        if check(int(input())):
            print('YES')
        else:
            print('NO')