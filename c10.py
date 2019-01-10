n=int(input())
a=1
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,n-2):
	c=a+b
	a=b
	b=c
	if i==n-3:
		print(c)
	else:
		print(c,end=" ")

