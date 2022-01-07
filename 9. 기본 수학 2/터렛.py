for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2=map(int,input().split())
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
        continue
    elif d<r1+r2 and d>abs(r1-r2):
        print(2)
        continue
    elif d==r1+r2 or d==abs(r1-r2):
        print(1)
        continue
    else:
        print(0)