from itertools import combinations

N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]

result = []
for card in cards:
    max_value = 0
    for comb in combinations(card, 3):
        total = sum(comb)
        max_value = max(max_value, total % 10)

    result.append(max_value)


max_idx = 0
for i in range(N):
    if result[i] >= result[max_idx]:
        max_idx = i

print(max_idx + 1)