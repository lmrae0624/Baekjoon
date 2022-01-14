def bfs(tomato_list):
    move_list=[(0,1),(1,0),(-1,0),(0,-1)]

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+move_list[i][0]
            ny=y+move_list[i][1]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato_list[nx][ny]==-1:
                continue
            if tomato_list[nx][ny]==0:
                tomato_list[nx][ny]=tomato_list[x][y]+1
                queue.append((nx,ny))
                
    for i in tomato_list:
        if 0 in i:
            return print(-1)
    return print(max(map(max, tomato_list))-1)

from collections import deque

m, n =map(int,input().split())
tomato_list=[]
queue=deque()
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 1:
            queue.append([i,j])
    tomato_list.append(row)

bfs(tomato_list)