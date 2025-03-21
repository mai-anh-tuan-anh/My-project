n=int(input())
cnt4=0
cnt7=0
while n>0:
    num=n%10
    n//=10
    if num==4: cnt4+=1
    if num==7: cnt7+=1
if(cnt4+cnt7==4 or cnt4+cnt7==7):
    print('YES')
else:
    print('NO')        
