a=int(input())
x=a//5
while x>=0:
    if (a-5*x)%3==0 :
        break
    x-=1  
print("-1" if x==-1 else x+(a-5*x)//3)