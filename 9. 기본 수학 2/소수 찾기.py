import math
a= int(input())
nlist=list(map(int,input().split()))
for i in range(a):

    if nlist[i]==1 or nlist[i]%2==0 and nlist[i]!=2:
        nlist[i]='-1'
        continue

    for j in range(2,math.ceil(math.sqrt(nlist[i])+1)):
        if nlist[i]%j==0 and nlist[i]!=2:
            nlist[i]='-1'
            break
rlist=[s for s in nlist if '-1'==s] 

print(len(nlist)-len(rlist))