n,m=map(int,input().split())
a=input().split()
def cal(arr):
    temp=arr[::-1]
    st=[]
    while(len(temp)>0):
        x=temp.pop()
        if(x=='*'):
            y=temp.pop()
            x=st.pop()
            st.append(int(x)*int(y))
        else:
            st.append(x)
    total=int(st[0])
    for i in range(1,len(st),2):
        op=st[i]
        num=int(st[i+1])
        if op=='+':
            total+=num
        else:
            total-=num
    return total
ok=False
def Try(arr,i):
    if i==n:
        if(cal(arr)==m):
            global ok
            ok=True
            for x in arr:
                if(len(x)>1 and x[0]=='-'):
                    print(f"({x})",end='')
                else:
                    print(f"{x}",end='')
            print(f"={m}")
        return
    for op in '+-*':
        Try(arr+[op,a[i]],i+1)
if __name__=='__main__':
    Try([a[0]],1)
    if not ok:
        print('IMPOSSIBLE')