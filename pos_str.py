a=input()
b=input()
p=0
l=[]
for i in range(0,len(a)):
    if a[i]==" ":
        y=a[p:i]
        l.append(y)
        p=i+1
r=a[p::]
l.append(r)
print((l.index(b))+1)
#pos
