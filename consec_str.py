n=int(input())
l=[]
c=0
for i in range(0,n):
	s=input()
	l.append(s)
for i in range(0,len(l)-1):
	if l[i]==l[i+1]:
		c=1
		break
if c==1:
	print("yes")
else:
	print("no")
  #consecutive
