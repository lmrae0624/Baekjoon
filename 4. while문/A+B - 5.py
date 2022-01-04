while(True):
    x, y= map(int,input().split())
    if x==0 and y==0:
        break
    print(x+y)

while(True):
    try:
        x, y= map(int,input().split())
        print(x+y)  
    except:
        break