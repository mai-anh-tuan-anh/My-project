n=int(input())
a=[]
def solanchuyen(s,target):
    if s==target: return 0
    for i in range(1,len(s)):
        if(s[i:]+s[:i]==target): return i
    return -1
if __name__=='__main__':
    for t in range(n):
        a.append(input())
    res=10**9
    for i in range(len(a)):
        cnt=0
        ok=True
        for j in range(len(a)):
            if(i!=j):
                num=solanchuyen(a[j],a[i])
                if(num==-1): 
                    ok=False
                    break
                cnt+=num
        if ok:
            res=min(res,cnt)
    print(res if res!=10**9 else '-1')