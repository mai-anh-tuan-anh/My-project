n=int(input())
st=set()
while len(st)<n:
    st.update(list(map(int,input().split())))
ok=True
for i in range(1,max(st)):
    if i not in st:
        ok=False
        print(i)
if ok:
    print('Excellent!')