import sys
k, n = map(int,sys.stdin.readline().rstrip().split())
line=[]
for _ in range(k):
    line.append(int(sys.stdin.readline().rstrip()))

start=1
end=max(line)
while start<=end:
    mid=(start+end)//2

    tmp=0
    for l in line:
        tmp+=l//mid
    #cnt = sum([l//mid for l in line])

    if tmp<n:
        end=mid-1
    elif tmp>=n:
        result=mid
        start=mid+1

print(result)