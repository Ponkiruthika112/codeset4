n=input()
l=list(map(int,input().split()))
k=list(set(l))
p=[]
s=""
for i in range(0,len(k)):
    p.append([k[i],l.index(k[i])])
p.sort(key=lambda x:x[1])
for i in range(0,len(p)):
    s=s+str(p[i][0])+" "
print(s.strip())
#unique
