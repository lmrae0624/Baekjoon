import sys
n=int(sys.stdin.readline().strip())
array=[]
for _ in range(n):
    array.append(int(sys.stdin.readline().strip()))

array[0]=[array[0],array[0]]
if n>1:
    array[1]=[array[1],array[0][0]+array[1]]

for i in range(2,n):
    array[i]=[array[i]+max(array[i-2]),array[i]+array[i-1][0]]

print(max(array[n-1]))