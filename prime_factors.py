# your code goes here
def prime(n):
	if n==2:
		return 1
	elif n==1:
	    return 0
	else:
		for i in range(2,n):
			if n%i==0:
				break
		if i==n-1:
			return 1
		else:
			return 0
n=int(input())
l=[]
for k in range(1,(n//2)+1):
	if n%k==0:
		l.append(k)
l.append(n)
s=""
for j in l:
    h=prime(j)
    if h==1:
        s=s+str(j)+" "
print(s.strip())
#prime factors
