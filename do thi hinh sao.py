n=int(input())
adj=[[] for x in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
adj=list(sorted(adj,key=lambda x:-len(x)))
if len(adj[0])!=n-1:
    print('No')
else:
    print('Yes')