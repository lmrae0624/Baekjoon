from string import ascii_lowercase
list=list(ascii_lowercase)
index=0
for s in input():
    if s in list:
        list[list.index(s)]=index
    index+=1
for l in list:
    if str(l).isdigit():
        print(l,end=" ")
    else:
        print("-1", end=" ")   

# find썼으면 간단....
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')