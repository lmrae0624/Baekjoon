a,b=map(int,input().split())
x,y=map(int,input().split())
i,j=map(int,input().split())
xlist=[a,x,i]
ylist=[b,y,j]
for q in xlist:
    if xlist.count(q)==1 :
        m=q
for p in ylist:
    if ylist.count(p)==1 :
        n=p
print(m,n)

x=y=0
i=j=0
exec("a,b=map(int,input().split());x^=a;y^=b;"*3)
print(x,y)