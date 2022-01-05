# import sys #시간초과
# for i in range(int(sys.stdin.readline())):
#     a,b = map(int,sys.stdin.readline().split())
#     distance=b-a-2
#     k=2
#     temp=2
#     while distance>0 :
#         if distance>2*k:
#             distance-=2*k
#             k+=1
#             temp+=2
#         elif distance==k or distance==k-1:
#             temp+=1
#             break
#         elif distance>=2*(k-1) and distance<=2*k :
#             temp+=2
#             break
#     print(1 if b-a==1 else temp)


import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    k=1
    distance=(b-a)/2 -k
    while distance>0 :
        k+=1
        distance-=k

    if distance<0 : 
        k-=1

    total=2*k+1 if distance<0 else 2*k

    temp=0 #지금 k가 차지하는 거리 구하기
    for j in range(1,k+1):
        temp+=j
        
    temp=temp*2+k+1 if total%2==1 else 2*temp 
    if temp < b-a:
        total+=1
    
    print(total)
 
       
import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 0

    num = math.floor(math.sqrt(distance))   # n제곱 <= 거리 < (n+1)제곱일때 n제곱
    num_square = num ** 2   # n제곱의 제곱
    increase_num = math.sqrt(num_square)

    if distance > num_square + increase_num:
        count = 2 * num + 1
    elif distance > num_square and distance <= num_square + increase_num:
        count = 2 * num
    elif distance == num_square:
        count = 2 * num - 1

    if distance < 4:
        count = distance

    print(count)