import sys
n=int(sys.stdin.readline().strip())
house=[]
for _ in range(n):
    house.append(list(map(int,sys.stdin.readline().strip().split())))

for i in range(1,n):
    for j in range(3):
        house[i][j]=min(house[i-1][j-1]+house[i][j],house[i-1][j-2]+house[i][j])

print(min(house[n-1]))