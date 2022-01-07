for i in range(int(input())):
    a=int(input())
    arr = [False, False] + [True] *(a-1)
    for i in range(2, int(a**0.5)+1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    
    for i in range(a//2,a+1):
        if arr[i]:
            if arr[a-i]:
                print(a-i,i)
                break