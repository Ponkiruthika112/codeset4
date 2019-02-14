n=int(input())
l=list(map(int,input().split()))
s=""
c=0
k=100000
for i in range(0,len(l)-1):
        c=l[i]-l[i+1]
        if k<c:
                print(l[i])
                break
        k=c
                

#print max
