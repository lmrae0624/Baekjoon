a=int(input())
arr = [False, False] + [True] *(a-1)
for i in range(2, int(a**0.5)+1):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

for j in range(len(arr)):
    if arr[j]:
        while a%j==0:
            a/=j
            print(j)


arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i): #앞에 항부터 확인해서 곱하기2 값은 false로 바꾸기
            arr[j] = False


while True:
    a=int(input())
    if a==0: break
    b=2*a
    arr = [False, False] + [True] *(b-1)
    for i in range(2, int(b**0.5)+1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    
    temp=0
    for j in range(a+1,b+1):
        if arr[j]:
            temp+=1
    print(temp)

for i in range(int(input())): 
    arr = [False, False] + [True] *(a-1) #10000까지니까 10000개로 고정적으로 만들고 for밖으로 빼도됨
    for i in range(2, int(a**0.5)+1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    a=int(input())
    for i in range(a//2,a+1):
        if arr[i]:
            if arr[a-i]:
                print(a-i,i)
                break