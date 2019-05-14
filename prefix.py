# your code goes here
n=int(input())
l=list(map(int,input().split()))
s=0
k=""
for i in range(0,len(l)):
	s=s+l[i]
	k=k+str(s)+" "
print(k.strip())
#prefix
