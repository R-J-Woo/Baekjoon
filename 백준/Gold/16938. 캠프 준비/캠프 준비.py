from itertools import combinations

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

result = 0

for count in range(2, len(A) + 1):
    for comb in combinations(A, count):
        if sum(comb) < L:
            continue
        if sum(comb) > R:
            continue
        if abs(max(comb) - min(comb)) < X:
            continue

        result += 1

print(result)