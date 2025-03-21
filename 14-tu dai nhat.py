import sys
s=sys.stdin.readline().split()
res=''
for sen in s:
    if(len(sen)>len(res)):
        res=sen
print(res,len(res))