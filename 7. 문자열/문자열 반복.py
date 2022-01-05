import sys  
a=int(sys.stdin.readline())
for i in range(a):
    b,s=map(str,sys.stdin.readline().split())
    for i in s:
        print(i*int(b), end="")
    print()