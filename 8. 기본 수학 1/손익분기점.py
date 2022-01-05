import math
import sys
a,b,c= map(int,sys.stdin.readline().split())
print(-1 if b-c==0 or a/(c-b)<0  else "%d" %(math.ceil(a/(c-b))) if a%(c-b)>0 else "%d" %(a/(c-b)+1))

a,b,c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)