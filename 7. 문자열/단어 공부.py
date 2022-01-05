a=input().lower()
alist=list(range(len(a)))
result=0
b=0
for i in set(a):
    if result<a.count(i):
        b=0
        result=a.count(i)
        alphabet=i
    elif result==a.count(i):
        b+=1
if b>0:
    alphabet="?"
print(alphabet.upper())

s,a=input().lower(),[]
for i in range(97,123):
 a.append(s.count(chr(i)))
print('?' if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())