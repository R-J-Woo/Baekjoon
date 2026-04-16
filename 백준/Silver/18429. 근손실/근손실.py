from itertools import permutations

N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 0
for perm in permutations(A):
    weight = 500
    flag = True
    for w in perm:
        weight -= K
        weight += w

        if weight < 500:
             flag = False

    if flag:
        result += 1


print(result)