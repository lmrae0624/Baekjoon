import sys
n, c= map(int,sys.stdin.readline().rstrip().split())
house=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
house.sort()

start=house[0]
end=house[-1]

def binary(start,end):
    mid=(start+end)//2

    if mid in house:
        return True
    else:
        return mid
        