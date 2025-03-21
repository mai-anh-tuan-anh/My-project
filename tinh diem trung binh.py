n=int(input())
a=list(map(float,input().split()))
b=[]
Max=max(a)
Min=min(a)
for i in a:
    if(i==Max or i==Min):
        continue
    else:
        b.append(i)
tong=float(0)
for i in b:
    tong+=i
print("%.2f" %(tong/len(b)))