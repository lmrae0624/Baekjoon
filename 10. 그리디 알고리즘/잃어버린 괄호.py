t=input()
templist=t.split(sep='-')
result=sum(list(map(int,templist[0].split(sep='+'))))
for temp in templist[1:]:
    a=sum(list(map(int,temp.split(sep='+'))))
    result-=a
print(result)