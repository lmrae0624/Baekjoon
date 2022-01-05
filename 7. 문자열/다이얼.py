a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result=0
for i in input():
    for j in a:
        if i in j:
            result+=a.index(j)+3
print(result)