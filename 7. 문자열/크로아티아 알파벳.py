a=['c=','c-','dz=','d-','lj','nj','s=','z=']
i=input()
for x in a:
    if x in i:
        i=i.replace(x,'1')
print(len(i))

w=input()
print(len(w) - sum(w.count(a)for a in['=','-','lj','nj','dz=']))