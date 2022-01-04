a=list(range(0,10))
for i in range(10):
    a[i]=int(input())%42
b = [int(input())%42 for i in range(10)]
print(len(set(a)))