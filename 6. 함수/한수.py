# a=int(input())
# if a<100:
#     print(a)
# else:
#     count=99
#     check=0
#     for i in range(100,a+1):
#         x=int(list(str(i))[1])
#         gap=x-int(list(str(i))[0])

#         for j in list(str(i))[2:]:
#             if int(j)-x !=gap:
#                 check=0
#                 break
#             else:
#                 check+=1
#             x=int(j)
#         if check!=0:
#             count+=1
#     print(count)
# 어차피 999까지만 보면 됐음.....

print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))
