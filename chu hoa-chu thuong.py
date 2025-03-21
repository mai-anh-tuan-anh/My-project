s=input()
lst=list(s)
Hoa=0
Thuong=0
for i in range(0,len(lst)):
    if(lst[i]>='a' and lst[i]<='z'):
        Thuong+=1
    else:
        Hoa+=1
if(Thuong>=Hoa): s=s.lower()
else: s=s.upper()
print(s)
