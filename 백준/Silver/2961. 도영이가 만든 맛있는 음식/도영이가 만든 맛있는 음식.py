from itertools import combinations

N = int(input())
flavors = []
for _ in range(N):
    flavors.append(list(map(int, input().split())))

result = int(1e9)
for i in range(1, N + 1):
    for c in combinations(flavors, i):
        s, b = 1, 0
        for f in c:
            s *= f[0]
            b += f[1]

        result = min(result, abs(s - b))

print(result)