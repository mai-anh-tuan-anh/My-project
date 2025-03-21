n, m, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
visited = [False] * (n + 1)
def bfs(start):
    queue = [start]
    visited[start] = True
    while queue:
        node = queue.pop(0)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

bfs(x)
not_connected = [i for i in range(1, n + 1) if not visited[i]]
if not not_connected:
    print(0)
else:
    for node in not_connected:
        print(node)