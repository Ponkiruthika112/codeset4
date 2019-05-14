# your code goes here
n=int(input())
l=list(map(int,input().split()))
l.remove(min(l))
print(sum(l))
#max sum
