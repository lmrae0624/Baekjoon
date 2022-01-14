# n, m ,v=map(int,input().split())
# edgelist=[]
# for _ in range(m):
#     edgelist.append(list(map(int,input().split())))
# edgelist.sort()

# visited=[False]*n

# def dfs(v):
#     visited[v-1]=True
#     print(v, end=' ')

#     for i in edgelist:
#         if i[0]==v and visited[i[1]-1] ==False:
#             dfs(i[1])
#         if i[1]==v and visited[i[0]-1]==False: 
#             dfs(i[0])
# dfs(v)
# print()
# from collections import deque
# def bfs(v):
#     queue = deque([v])
#     visited[v-1]=False

#     while queue:
#         v=queue.popleft()
#         print(v, end=' ')
        
#         for i in edgelist:
#             if i[0]==v and visited[i[1]-1]==True:
#                 queue.append(i[1])
#                 visited[i[1]-1]=False
#             if i[1]==v and visited[i[0]-1]==True: 
#                 queue.append(i[0])
#                 visited[i[0]-1]=False
# bfs(v)

N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(v):
    visit_list[v]=1
    print(v, end=' ')

    for i in range(1,N+1):
        if matrix[v][i]==1 and visit_list[i]==0 :
            dfs(i)
dfs(V)
print()

from collections import deque
def bfs(v):
    queue = deque([v])
    visit_list[v]=0

    while queue:
        v=queue.popleft()
        #q = tmp.pop(0) popleft대체로 사용 가능
        print(v, end=' ')

        for i in range(1,N+1):
            if matrix[v][i]==1 and visit_list[i]==1 :
                queue.append(i)
                visit_list[i]=0

bfs(V)