n=input()
l=list(map(int,input().split()))
s=0
k=""
for i in range(0,len(l)):
	s=s+l[i]
	if l[i]%2==0:
		k=k+str(s)+" "
	else:
		k=k+str(l[i])+" "
print(k.strip())
#prefix sum
