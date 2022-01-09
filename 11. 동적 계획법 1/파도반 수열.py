import sys
t=int(sys.stdin.readline().strip())

nlist=[int(sys.stdin.readline().strip()) for _ in range(t)]

array=[0,1,1,1,2]
for i in range(5,max(nlist)+1):
    array.append(array[i-1]+array[i-5])

for n in nlist:
    print(array[n])