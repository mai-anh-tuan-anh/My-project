x=input()
st=set()
while len(x)>0:
    num=x[:2]
    if num not in st and len(num)==2:
        st.add(num)
        print(num,end=' ')
    x=x[2:]