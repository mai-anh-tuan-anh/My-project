def DFS(u,visited,adj):
    visited[u]=1
    for v in adj[u]:
        if(not visited[v]):
            DFS(v,visited,adj)
if __name__=='__main__':
    for t in range(int(input())):
        n,m=map(int,input().split())
        adj=[[] for x in range(n+1)]
        for i in range(m):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        able=False
        tplt=0
        res=[]
        visited=[0]*(n+1)
        for i in range(1,n+1):
            if(not visited[i]):
                tplt+=1
                DFS(i,visited,adj)
        M=tplt
        for i in range(1,n+1):
            visited=[0]*(n+1)
            visited[i]=1
            current=0
            for j in range(1,n+1):
                if(not visited[j]):
                    current+=1
                    DFS(j,visited,adj)
            if current>tplt:
                able=True
                if(current>M):
                    M=current
                    res.clear()
                    res.append(i)
                elif current==M:
                    res.append(i)
        res=sorted(res)
        print(res[0] if able else '0')