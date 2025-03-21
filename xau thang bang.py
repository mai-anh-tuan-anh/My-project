from math import *
mau='abcdefghijklmnopqrstuvwxyz'
P=list(mau)
for t in range(int(input())):
    s=input()
    rev_s=s[::-1]
    ok=True
    for i in range(1,ceil(len(s)/2)):
        s11=P.index(s[i])
        s12=P.index(s[i-1])
        s21=P.index(rev_s[i])
        s22=P.index(rev_s[i-1])
        if(abs(s11-s12)!=abs(s21-s22)):
            ok=False
            print('NO')
            break
    if ok:
        print('YES')
