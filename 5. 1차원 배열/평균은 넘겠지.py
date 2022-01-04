a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    count=0
    for i in b[1:]:
        if i > sum(b[1:])/b[0] : count +=1
    print( "%.3f%%" % (count/b[0]*100))