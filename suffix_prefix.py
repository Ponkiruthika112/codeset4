n=int(input())
l=list(map(int,input().split()))
k=[]
p=0
d=[]
r=""
for i in range(0,len(l)):
    p=p+l[i]
    k.append(p)
d=k[::-1]
if len(k)==1:
    r=str(l[0])
else:
    for i in range(0,len(k)):
        r=r+str(k[i]+d[i])+" "
print(r.strip())
#v

#suffix prefix
