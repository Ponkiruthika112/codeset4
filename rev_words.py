s=input()
l=s.split()
k=""
for i in l:
    k=k+i[::-1]+" "
print(k.strip())
#reverse words
