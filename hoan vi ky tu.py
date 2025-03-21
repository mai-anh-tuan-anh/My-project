from itertools import *
lst=list(input())
perm=permutations(lst)
for lt in perm:
    print("".join(lt))