res=[]
a=[]
def Try(sum,n):
    if sum>n: return
    if sum==n: 
        res.append(a[:])
        return
    for i in range(n,0,-1):
        a.append(i)
        Try(sum+i,n)
        a.pop()
if __name__=='__main__':
    for t in range(int(input())):
        res.clear()
        a.clear()
        n=int(input())
        Try(0,n)
        st=set()
        for item in res:
            item=sorted(item,reverse=True)
            st.add(tuple(item))
        st=list(sorted(st,key=lambda x:x,reverse=True))
        print(len(st))
        for i in st:
            print('(',end='')
            print(*i,end='')
            print(')',end=' ')
        print()
            