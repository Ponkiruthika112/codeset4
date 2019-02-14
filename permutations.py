from itertools import permutations
s=input()
p=list(permutations(s))
k=list(set(p))
for i in range(0,len(k)):
        print("".join(k[i]))
#permutation
