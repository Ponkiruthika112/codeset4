s=input()
i=0
k=""
while i<len(s):
	n=int(s[i+1])
	if n%2==0:
		k=k+n*s[i]
	else:
		k=k+s[i]+s[i+1]
	i=i+2
print(k)
#encode
