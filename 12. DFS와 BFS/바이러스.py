computer= int(input())
edge=[[0]*(computer+1) for _ in range(computer+1)]
for _ in range(int(input())):
    a, b= map(int,input().split())
    edge[a][b]=edge[b][a]=1

visited=[0]*(computer+1)
def bfs(v):
    queue=[]
    queue.append(v)
    visited[v]=1

    while queue:
        v=queue.pop(0)

        for i in range(1,computer+1):
            if edge[v][i]==1 and visited[i]==0:
                queue.append(i)
                visited[i]=1
bfs(1)
print(sum(visited)-1)
