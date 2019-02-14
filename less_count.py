n,k=input()
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)-1):
        for j in range(0,len(l)):
                if l[i]<l[j]:
                        c=c+1
print(c)
#leess one
