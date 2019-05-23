s=input()
k=s.replace(" ","")
p=""
for i in range(1,len(k)+1):
    if i%2!=0:
        p=p+k[i-1].upper()
    else:
        p=p+k[i-1]
for i in range(0,len(s)):
    if s[i]==" ":
        p=p[0:i]+" "+p[i::]
print(p)
#caps in odd
