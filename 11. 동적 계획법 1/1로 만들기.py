import sys
n=int(sys.stdin.readline().strip())

d=[0]*(n+1)
d[0]=0
d[1]=0
for i in range(2,n+1):
    if i==2 or i==3:
        d[i]=1
        continue

    d[i]=d[i-1]+1

    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
print(d[n])


s={1:0,2:1}

def f(n):
 if n in s:
  return s[n]
 m=1+min(f(n//2)+n%2,f(n//3)+n%3)
 s[n]=m
 print(s)
 return m
print(f(int(input())))