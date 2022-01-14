from collections import deque
m, n , h =map(int,input().split())
tomato_list=[]
queue=deque()

for i in range(h):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k]==1:   
                queue.append((i,j,k))
    tomato_list.append(tmp)

def bfs(tomato_list):
    move_x=[-1,1,0,0,0,0]
    move_y=[0,0,1,-1,0,0]
    move_z=[0,0,0,0,1,-1]
    count=0

    while queue:
        count+=1
        for _ in range(len(queue)):
            x,y,z=queue.popleft()
            for i in range(6):
                nx=x+move_x[i]
                ny=y+move_y[i]
                nz=z+move_z[i]
                
                if 0<=nx<h and 0<=ny<n and 0<=nz<m and tomato_list[nx][ny][nz]==0:
                    queue.append((nx,ny,nz))
                    tomato_list[nx][ny][nz]=tomato_list[x][y][z]+1

    for i in range(len(tomato_list)):
        for j in range(len(tomato_list[i])):
            if 0 in tomato_list[i][j]:
                return -1
    return count-1
print(bfs(tomato_list))


# day = 0
# for i in tomato_list:
#     for j in i:
#         for k in j:
#             if k==0:
#                 print(-1)
#                 exit(0)
#         day = max(day,max(j))
# print(day-1)
 
#기존에 푼거
# from collections import deque
# m, n , h =map(int,input().split())
# #tomato_list=[[[0 for col in range(m)] for row in range(n)] for depth in range(h)]
# tomato_list=[]
# queue=deque()
# for i in range(h):
#     for j in range(n):
#         tomato=list(map(int,input().split()))
#         for k in range(m):
#             if tomato[k]==1:   
#                 queue.append((j,k,i))
#             tomato_list[i][j][k]=tomato[k]

#틀린 부분 
#max(map(max,(map(max, tomato_list))))-1
#왜틀린진 모른다......