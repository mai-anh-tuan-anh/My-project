n=int(input())
def adj_list(adj):
    for i in range(1,n+1):
        print('adj({}): = ({})'.format(i,adj[i]))
def edge_list(adj):
    for i in range(1,n+1):
        for j in adj[i]:
            print(i,j)
def adj_matrix(adj):
    matrix=[]
    for i in range(n):
        matrix.append([0]*n)
    for i in range(1,n+1):
        for j in adj[i]:
            matrix[i-1][j-1]=1
    for i in range(n):
        print(*matrix[i])
if __name__=='__main__':
    adj=[]
    adj.append(0)
    for i in range(n):
        adj.append(list(map(int,input().split())))
    choice=int(input())
    if choice==1:
        adj_list(adj)
    elif(choice==2):
        edge_list(adj)
    else:
        adj_matrix(adj)