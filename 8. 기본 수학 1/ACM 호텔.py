for i in range(int(input())):
    h,w,n= map(int,input().split())
    if n%h==0:
        a=h
        b=str(n//h).zfill(2)
    else :
        a=n%h
        b=str(n//h+1).zfill(2)
    print(a,b,sep="")


import sys
for t in range(2):
    h, w, n = map(int, sys.stdin.readline().split())
    print("%d%02d" % ((n-1)%h+1, (n-1)//h+1))