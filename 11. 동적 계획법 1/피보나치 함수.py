import sys
t=int(sys.stdin.readline().strip())
nlist=[int(sys.stdin.readline().strip()) for _ in range(t)]

d=[0]*41
d[0]=[1,0]
d[1]=[0,1]
#d = [[1,0], [0,1]] 이렇게 하고 append해주기

for i in range(2,max(nlist)+1):
    d[i]=[d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1]]

for n in nlist:
    print(d[n][0],d[n][1])
    