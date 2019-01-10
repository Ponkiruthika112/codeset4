s=input()
s=s.strip()
k=len(s)
c=0
sp=s.count(" ")
for i in s:
  if i.isalpha():
    c=c+1
  elif i.isdigit():
    c=c+1
print(k-c-sp)
