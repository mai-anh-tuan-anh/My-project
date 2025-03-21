n=int(input())
m=int(input())
adj=[[] for x in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
visited=[False]*(n+1)
def BFS(S):
    q=[S]
    res=[]
    visited[S]=True
    while len(q):
        u=q.pop(0)
        res.append(u)
        for v in adj[u]:
            if not visited[v]:
                q.append(v)
                visited[v]=True
    return res
if __name__=='__main__':
    do_thi_con=[]
    for i in range(1,n+1):
        if not visited[i]:
            do_thi_con.append(BFS(i))
    ok=True
    for dothi in do_thi_con:
        for u in dothi:
            if len(adj[u]) != len(dothi)-1:
                ok=False
                break
    print('YES' if ok else 'NO')