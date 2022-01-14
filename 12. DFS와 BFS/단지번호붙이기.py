n=int(input())
house_list=[list(map(int,input())) for _ in range(n)]

house_count=0
danji=0
def dfs(x,y):
    global house_count
    if x<0 or x>=n or y<0 or y>=n:
        return False

    if house_list[x][y]==1:
        house_list[x][y]=0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        house_count+=1
    return house_count

house_count_list=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j)!=False:
            danji+=1
            house_count_list.append(dfs(i,j))
        house_count=0

print(danji)
house_count_list.sort()
for i in house_count_list:
    print(i)

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
