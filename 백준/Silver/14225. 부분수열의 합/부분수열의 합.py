from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

numbers = set()
for i in range(1, len(S) + 1):
    for comb in combinations(S, i):
        numbers.add(sum(comb))

count = 1
while True:
    if count not in numbers:
        print(count)
        break

    count += 1