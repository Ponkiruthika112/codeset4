n,k=map(int,input().split())
l=[]
for i in range(0,n):
	s=input()
	if (s.count("a")>=1 or s.count("e")>=1 or s.count("i")>=1 or s.count("o")>=1 or s.count("u")>=1):
		l.append("1")
if(l.count("1")>=k):
	print("yes")
else:
	print("no")
#atmost
