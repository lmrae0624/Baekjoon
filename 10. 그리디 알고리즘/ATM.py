int(input())
timelist=list(map(int,input().split()))
timelist.sort()

result=0
for i in range(len(timelist)):
    result+=sum(timelist[:i+1])
print(result)