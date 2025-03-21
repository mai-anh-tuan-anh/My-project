from math import *
def nt(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,isqrt(n)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
if __name__=='__main__':
    n,m=map(int,input().split())
    st=set()
    M=-1
    for i in range(n):
        b=list(map(int,input().split()))
        for j in range(m):
            if(nt(b[j]) and b[j]>M):
                M=b[j]
                st.clear()
                st.add((i,j))
            elif b[j]==M:
                st.add((i,j))
    if M==-1:
        print('NOT FOUND')
    else:
        print(M)
        st=sorted(st,key=lambda x:(x[0],x[1]))
        for item in st:
            print("Vi tri [{}][{}]".format(item[0],item[1]))