n,k=map(int,input().split())
l=list(map(int,input().split()))
m=max(l)
val=k
while val<=m:
	val=val+1
	if(l.count(val)>=1):
		print(val)
		break
else:
	print("no")
#max_of_given_nor
