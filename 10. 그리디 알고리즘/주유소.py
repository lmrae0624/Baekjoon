# 17점
n=int(input())
distance_list=list(map(int,input().split()))
cost_list=list(map(int,input().split()))

mincost=min(cost_list[:-1])
totaldis=sum(distance_list)
totalcost=0
for i in range(len(distance_list)):
    
    if cost_list[i]==mincost:
        totalcost+=totaldis*mincost
        break
    totalcost+=distance_list[i]*cost_list[i]
    totaldis-=distance_list[i]
print(totalcost)

#100점
n = int(input())
cities = list(map(int, input().split()))
prices = list(map(int, input().split()))

ans = 0
min_price = prices[0]

for i in range(n-1):
    if prices[i] < min_price:
        min_price = prices[i]

    ans += min_price * cities[i]
print(ans)