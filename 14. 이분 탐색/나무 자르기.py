import sys
n, m= map(int,sys.stdin.readline().rstrip().split())
tree=list(map(int,sys.stdin.readline().rstrip().split()))

start=1
end=max(tree)
#s, e = 0, max(woods)[0]

result=0
while start<=end:
    mid=(start+end)//2

    cnt=sum([(t-mid) for t in tree if (t-mid) > 0])
    cnt=sum([(t-mid) for t in tree if t > mid])

    if cnt<m:
        end=mid-1
    elif cnt>=m:
        result=mid
        start=mid+1
print(result)
