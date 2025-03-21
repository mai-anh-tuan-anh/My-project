n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
if n==m:
    for i in range(n):
        print(*a[i])
elif n<m:
    lt,cnt=1,0
    st=set()
    while cnt<(m-n):
        st.add(lt)
        cnt+=1
        lt+=2
    for i in range(n):
        for j in range(m):
            if j not in st:
                print(a[i][j],end=' ')
        print()
else:
    lt,cnt=0,0
    st=set()
    while cnt<(n-m):
        st.add(lt)
        cnt+=1
        lt+=2
    for i in range(n):
        if i not in st:
            for  j in range(m):
                print(a[i][j],end=' ')
            print()
        