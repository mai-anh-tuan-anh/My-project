s=input()
n=0
for i in s:
    n=n*2+int(i)
res=''
while n>0:
    res+=str(n%8)
    n//=8
res=res[::-1]
print(res)