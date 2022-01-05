for t in range(int(input())):
    x=int(input())
    y=int(input())
    alist=[i for i in range(1,y+1)]
    for i in range(x):
        a=1
        for j in range(1,y):
            alist[j]=alist[j]+a
            a=alist[j]
    print(a)