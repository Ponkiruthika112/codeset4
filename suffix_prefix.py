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
for i in range(0,len(k)):
    r=r+str(k[i]+d[i])+" "
print(r.strip())


#suffix prefix
