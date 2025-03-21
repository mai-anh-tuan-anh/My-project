from math import*
def nguyento(n):
    if n<=1: return False
    if n<=3: return True
    if (n%2==0) or (n%3==0): return False
    for i in range(5,isqrt(n),6):
        if (n%i==0) or (n%(i+2)==0):
            return False
    return True
def check(n):
    lst=list(n)
    tong=0
    for i in range(len(lst)):
        if i%2!=int(lst[i])%2:
            return False
        tong+=int(lst[i])
    return nguyento(tong)
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')
        