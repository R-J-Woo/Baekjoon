from itertools import permutations

A, B = input().split()

s = set()
for perm in permutations(A):
    num = ''.join(perm)
    if num[0] == '0' or int(num) >= int(B):
        continue
    
    s.add(num)

if len(s) > 0:
    print(int(max(s)))
else:
    print(-1)