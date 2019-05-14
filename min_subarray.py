n=int(input())
l=list(map(int,input().split()))
sublist=[0]
for i in range(0,len(l)+1):
	for j in range(i+1,len(l)+1):
		p=l[i:j]
		sublist.append(sum(p))
print(min(sublist))
#subarray
