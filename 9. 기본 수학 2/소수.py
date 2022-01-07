import math
a=int(input())
b=int(input())
nlist=[]
for i in range(a,b+1):
    if i==2: nlist.append(i); continue
    
    if i==1 or i%2==0 and i!=2:
        continue
    
    temp=0
    for j in range(2,math.ceil(math.sqrt(i)+1)):
        if i%j==0:
            temp+=1
            break
    
    if temp==0:
        nlist.append(i)

if len(nlist)==0:
    print(-1)
else:
    print(sum(nlist),nlist[0],sep="\n")