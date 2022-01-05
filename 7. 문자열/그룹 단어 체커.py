a=int(input())
b=a
for i in range(a):
    string=list(input())
    slist=[]
    temp=string[0]
    slist.append(temp)
    for s in string[1:]:
        if s != temp:
            if s in slist:
                b-=1
                break
            temp=s
            slist.append(s)
print(b)

T = int(input())
cnt = 0
for i in range(T):
    word = input()
    for j in range(len(word) - 1):
        if word.find(word[j]) > word.find(word[j + 1]): 
            # 지금 문자값 j의 인덱스 값 찾고 , j+1의 인덱스 값을 찾아서 비교 (find는 제일 처음 인덱스를 뽑아주니까)
            cnt += 1
            break
print(T - cnt)