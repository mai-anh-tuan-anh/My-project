from math import *
def nguyento(n):
    if n<=1: return False
    if n<=3: return True
    if (n%2==0) or (n%3==0): return False
    for i in range(5,isqrt(n)+1,6):
        if (n%i==0) or (n%(i+2)==0):
            return False
    return True
def check(n):
    lst=list(n)
    for i in range(len(lst)):
        if nguyento(i)!=nguyento(int(lst[i])):
            return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')