n=int(input())
timelist=[]
for _ in range(n):
    timelist.append(list(map(int,input().split())))

#이렇게 하면 sort만 써도 endtime기준으로 정렬하고 starttime으로 정렬 가능
# for _ in range(n):
#         s, e = map(int, input().split())
#         timelist.append((e, s))
# timelist.sort()

timelist = sorted(timelist, key = lambda x : (x[1], x[0]))

mintime=timelist[0]
result=1
for time in timelist[1:]:
    
    if mintime[1]<=time[0]:
        mintime=time
        result+=1

print(result)