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
    a=list(n)
    tong=0
    for i in range(len(a)):
        if(not nguyento(int(a[i]))): return False
        tong+=int(a[i])
    return nguyento(tong)
if __name__=='__main__':
    for t in range(int(input())):
        n=input()
        ok=False
        if(nguyento(int(n))):
            if(nguyento(int(n[::-1]))):
                if(check(n)):
                    ok=True
        print('Yes' if ok else 'No')