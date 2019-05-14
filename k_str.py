n,k=map(int,input().split())
l=[]
p=[]
c=0
for i in range(0,n):
	s=input()
	l.append(s)
for i in range(0,len(l)-1):
	if l[i]==l[i+1]:
		c=c+1
	else:
		p.append(c)
		c=0
if p.count(k)!=0:
	print("yes")
else:
	print("no")
  #kstring
