from collections import *
n,m=map(int,input().split())
a=dict(Counter(list(map(int,input().split()))))
a=sorted(a.items(),key=lambda x:(-x[1],x[0]))
st=set()
for i in a:
    st.add(i[1])
if(len(st)==1):
    print('NONE')
else:
    st=list(st)
    largest=max(st)
    st.remove(largest)
    second_largest=max(st)
    for i in a:
        if i[1]==second_largest:
            print(i[0])
            break

