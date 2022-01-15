import sys
n=int(sys.stdin.readline().rstrip())
k=int(sys.stdin.readline().rstrip())

start=1
end=k
while start<=end:
    mid=(start+end)//2

    tmp=0
    for i in range(1,n+1):
        tmp += min(mid//i, n)

    if tmp >= k: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)