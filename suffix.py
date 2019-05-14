n=int(input())
l=list(map(int,input().split()))
s=0
k=""
d=[]
for i in range(len(l)-1,-1,-1):
    s=s+l[i]
    d.append(s)
for i in range(len(d)-1,-1,-1):
    k=k+str(d[i])+" "
print(k.strip())
#suffix
