import sys
n=int(sys.stdin.readline().strip())
tlist=[]
for _ in range(n):
    tlist.append(list(map(int,sys.stdin.readline().strip().split())))

for i in range(1,n):
    tlist[i][0]+=tlist[i-1][0]
    tlist[i][len(tlist[i])-1]+=tlist[i-1][len(tlist[i-1])-1]

    for j in range(1,len(tlist[i])-1):
        tlist[i][j]=max(tlist[i-1][j]+tlist[i][j],tlist[i-1][j-1]+tlist[i][j])

print(max(tlist[n-1]))


def solution():
    import sys
    n = int(input())
    triangle =[]
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))
                   
    accum = []
    for i in range(n):
        accum = [max(a+c, b+c) for a,b,c in zip([0]+accum, accum+[0], triangle[i])]
    print(max(accum))

solution()

## zip 코드 참고
# Number = [1,2,3,4]
# Name = ['hong','gil','dong','nim']
# Number_Name = list(zip(Number,name))
# print(Number_Name)
# '''
# 결과 : [(1 ,'hong'), (2 ,'gil'), (3 ,'dong'), (4 ,'nim')]