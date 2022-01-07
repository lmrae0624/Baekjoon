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