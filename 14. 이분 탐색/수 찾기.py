n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

nlist.sort()

def binary(array,find,start,end):
    if start>end:
        return False
    mid=(start+end)//2

    if find == array[mid]:
        return True
    elif find > array[mid]:
        return binary(array,find,mid+1,end)
    else:
        return binary(array,find,start,mid-1)

for ml in mlist:
    result=binary(nlist,ml,0,n-1)
    if result:
        print(1)
    else:
        print(0)
