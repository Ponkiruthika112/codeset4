from itertools import permutations
s=input()
k=list(permutations(s))
for i in range(0,len(k)):
        print("".join(k[i]))
#permutation
