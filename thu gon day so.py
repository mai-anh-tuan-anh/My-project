n=int(input())
a=list(map(int,input().split()))
st=[]
for i in range(n):
    ok=1
    if(len(st)>0 and (st[-1]+a[i])%2==0):
        st.pop()
        ok=0
    if ok:st.append(a[i])
print(len(st))