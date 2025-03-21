for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    st=[]
    res=[-1]*n
    for i in range(n):
        while(len(st)>0 and a[st[-1]]<=a[i]):
            st.pop()
        if(len(st)>0):
            res[i]=st[-1]
        st.append(i)
    for i in range(n):
        res[i]=i-res[i]
    print(*res)