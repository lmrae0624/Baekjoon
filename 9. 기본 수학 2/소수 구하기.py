import math
a,b=map(int,input().split())
nlist=[]
for i in range(a,b+1):
    if i==2: nlist.append(i); continue
    
    if i==1 or i%2==0 and i!=2:
        continue
    
    temp=0
    for j in range(2,math.ceil(math.sqrt(i)+1)):
        if i%j==0:
            temp+=1
            break
    if temp==0:
        nlist.append(i)

for l in nlist:
        print(l)


m, n = map(int, input().split())
li = [False] + [True] * ((n - 1) // 2)
for x in range(1, int(n**.5/2+1)): #제곱근까지만 확인하면 된다
  if li[x]: #li가 True 면
    li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1)) #start:end:step
if m <= 2: #2보다 작으면 소수 2출력 
  print(2)
print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val])) #val이 True면 x값 출력, 짝수는 어차피 소수아니라 확인 필요없음
#zip: 함수는 여러 개의 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
m, n = map(int, input().split())

def isprime(m, n):
  n += 1                            # for문 사용을 위한 n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)
isprime(m, n)