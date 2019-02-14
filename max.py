n=int(input())
l=list(map(int,input().split()))
s=""
for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
                s=s+str(l[i])+" "
        else:
                s=s+str(l[i+1])+" "
                
print(s.strip())
#max
