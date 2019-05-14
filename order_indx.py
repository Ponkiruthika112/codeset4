n=input()
k=list(map(int,input().split()))
s=""
p=[]
for i in range(0,len(k)):
    p.append([k[i],k.index(k[i])])
p.sort()
for i in range(0,len(p)):
    s=s+str(p[i][1]+1)+" "
print(s.strip())
    
    
#order
