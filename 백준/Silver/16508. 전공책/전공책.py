from itertools import combinations
from collections import Counter

target = input()
N = int(input())

books = []
for _ in range(N):
    price, title = input().split()
    books.append((int(price), title))

target_count = Counter(target)
answer = float('inf')

for k in range(1, N + 1):
    for comb in combinations(books, k):
        sum = 0
        alpha = Counter()

        for price, title in comb:
            sum += price
            alpha += Counter(title)

        flag = True
        for c in target_count:
            if alpha[c] < target_count[c]:
                flag = False
                break

        if flag:
            answer = min(answer, sum)

if answer == float('inf'):
    print(-1)
else:
    print(answer)