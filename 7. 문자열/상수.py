a,b=map(str,input().split())
a,b=a[::-1],b[::-1]
print(a if a>b else b)
print(max(a,b))