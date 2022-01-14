move_list=[(0,1),(1,0),(-1,0),(0,-1)]
def bfs(tomato_list):
    queue=[]

    x ,y=np.where(tomato_list==1)
    for i in range(len(x)):
        queue.append((x[i],y[i]))

    while queue:
        x,y=queue.pop(0)
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
    return tomato_list

from sys import stdin
import numpy as np

m, n =map(int,stdin.readline().split())
tomato_list=np.array([list(map(int,stdin.readline().split())) for _ in range(n)])

if 0 in bfs(tomato_list):
    print(-1)
else:
    print(max(map(max, tomato_list))-1)



    # if x-1>=0 and tomato_list[x-1][y]==0:
    #         tomato_list[x-1][y]=tomato_list[x][y]+1
    #         queue.append((x-1,y))
    #     if x+1<n and tomato_list[x+1][y]==0:
    #         tomato_list[x+1][y]=tomato_list[x][y]+1
    #         queue.append((x+1,y))
    #     if y-1>=0 and tomato_list[x][y-1]==0:
    #         tomato_list[x][y-1]=tomato_list[x][y]+1
    #         queue.append((x,y-1))
    #     if y+1<m and tomato_list[x][y+1]==0:
    #         tomato_list[x][y+1]=tomato_list[x][y]+1
    #         queue.append((x,y+1))