import sys
n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline())
mlist=list(map(int,sys.stdin.readline().rstrip().split()))
card={}
for n in nlist:
    if n not in card:
        card[n]=1
    else:
        card[n]+=1

# from collections import Counter
# counter = Counter(nlist)

for m in mlist:
    if m in card:
        print(card[m],end=' ')
    else:
        print(0,end=' ')

