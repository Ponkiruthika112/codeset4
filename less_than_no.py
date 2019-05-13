n,k=map(int,input().split())
l=list(map(int,input().split()))
if l.count(k)>=1:
	print(k)
else:
	m=min(l)
	val=k
	while val>m:
		val=val-1
		if(l.count(val)>=1):
			print(val)
			break
	else:
		if(l.count(m)>=1):
			print(m)
		else:
			print("no")

#leesss
