move_list=[(0,1),(1,0),(-1,0),(0,-1)]

def bfs(x,y,m,n):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    queue=[[x,y]]

    if bae_list[x][y]==1:
        while queue:
            x,y=queue.pop(0)  

            bae_list[x][y]=0
            for i in range(4):
                nx=x+move_list[i][0]
                ny=y+move_list[i][1]
                if nx>=0 and nx<m and ny>=0 and ny<n:
                    queue.append([nx,ny])
        return True

def bfs_1(x,y,m,n):
    queue=[[x,y]]

    if bae_list[x][y]==1:
        while queue:
            x,y=queue.pop(0)

            for i in range(4):
                nx=x+move_list[i][0]
                ny=y+move_list[i][1]

                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if bae_list[nx][ny]==0:
                    continue
                if bae_list[nx][ny]==1:
                    bae_list[nx][ny]=0
                    queue.append([nx,ny])
        return True

t=int(input())
for _ in range(t):
    m, n, k=map(int,input().split())
    bae_list=[[0]*n for _ in range(m)]
    for _ in range(k):
        x, y =map(int,input().split())
        bae_list[x][y]=1
    
    result=0
    for i in range(m):
        for j in range(n):
            if bfs(i,j,m,n)==True:
                result+=1
    print(result)