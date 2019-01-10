s=input()
s=s.strip()
k=len(s)
c=0
sp=s.count(" ")
for i in s:
  if i.isalpha():
    c=c+1
  elif i.isdigits():
    c=c+1
print(k-c-sp)
