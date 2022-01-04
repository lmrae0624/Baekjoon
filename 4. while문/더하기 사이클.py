x=int(input())
y=(x%10)*10+(x//10+x%10)%10
c=1
while y!=x:
    y=(y%10)*10+(y//10+y%10)%10
    c+=1
print(c)

x=int(input())
y=-1
c=0
while y!=x:
    if y==-1:
        y=x
    y=(y%10)*10+(y//10+y%10)%10
    c+=1
print(c)