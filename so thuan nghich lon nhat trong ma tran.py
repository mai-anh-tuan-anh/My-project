from math import *
def thuannghich(n):
    if len(n)<2: return False
    return n==n[::-1]
if __name__=='__main__':
    n,m=map(int,input().split())
    st=set()
    M=-1
    for i in range(n):
        b=list(map(int,input().split()))
        for j in range(m):
            if(thuannghich(str(b[j])) and b[j]>M):
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