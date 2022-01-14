n, m = map(int,input().split())
pan_list=[list(map(int,input())) for _ in range(n)]

move_list=[(0,1),(1,0),(-1,0),(0,-1)]
def bfs(x,y):
    queue=[(x,y)]
    
    while queue:
        x,y=queue.pop(0)

        for i in range(4):
            nx=x+move_list[i][0]
            ny=y+move_list[i][1]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if pan_list[nx][ny]==0:
                continue
            if pan_list[nx][ny]==1:
                pan_list[nx][ny]=pan_list[x][y]+1
                queue.append((nx,ny))
    return pan_list[n-1][m-1]      
print(bfs(0,0))