s=input()
p=s.count(" ")
n=len(s)-p
if n==2:
	print("yes")
else:
	for i in range(2,n):
		if n%i==0:
			break
	if i==n-1:
		print("yes")
	else:
		print("no")
#length
