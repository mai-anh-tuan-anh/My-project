s1=input().lower().split()
s2=input().lower().split()
hop=set()
st1,st2,giao=set(),set(),set()
for chr in s1:
    st1.add(chr)
    hop.add(chr)
for chr in s2:
    st2.add(chr)
    hop.add(chr)
for chr in st1:
    if chr in st2:
        giao.add(chr)
hop=sorted(hop,key=lambda x:x)
giao=sorted(giao,key=lambda x:x)
print(*hop)
print(*giao)