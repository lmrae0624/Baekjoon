alist=list()
for i in range(1, 10001):
    x=0
    for j in str(i):
        x+=int(j)
    alist.append(i+x)

set=set(alist)
for i in range(1, 10001):
    if i not in set:
        print(i)