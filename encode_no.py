s=input()
i=0
k=""
while i<len(s):
	n=int(s[i+1])
	k=k+n*s[i]
	i=i+2
print(k)
#encoding
