n, k =map(int,input().split())
coinlist=[]
for _ in range(n):
    coinlist.append(int(input()))

result=0
for coin in coinlist[::-1]:
    result+=k//coin
    k=k%coin

    if k==0:
        break
        
print(result)