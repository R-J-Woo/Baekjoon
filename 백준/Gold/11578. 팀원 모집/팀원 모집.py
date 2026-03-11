from itertools import combinations

N, M = map(int, input().split())
students = {}
for i in range(1, M + 1):
    prob = list(map(int, input().split()))
    students[i] = prob[1:]

result = M + 1
for i in range(1, M + 1):
    for comb in combinations(range(1, M + 1), i):
        total = set()
        for c in comb:
            for prob in students[c]:
                total.add(prob)

        if len(total) == N:
            result = min(result, i)

if result == M + 1:
    print(-1)
else:
    print(result)