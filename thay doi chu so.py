def pthanhq(a,b,p,q):
    a=a.replace(p,q)
    b=b.replace(p,q)
    return int(a)+int(b)
def qthanhp(a,b,p,q):
    a=a.replace(q,p)
    b=b.replace(q,p)
    return int(a)+int(b)
if __name__=='__main__':
    for t in range(int(input())):
        p,q=input().split()
        s=input().split()
        m='a'
        n='b'
        if(len(s)>1):
            m=s[0]
            n=s[1]
        else:
            m=s[0]
            n=input()
        print(qthanhp(m,n,p,q),pthanhq(m,n,p,q))