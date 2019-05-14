# your code goes here
n=int(input())
p=[]
l=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(0,len(k)):
	p.append([l[i],k[i]])
p.sort(key=lambda x:x[1])
s=""
for i in range(0,len(p)):
	s=s+str(p[i][0])+" "
print(s.strip())
#based on weights ki
