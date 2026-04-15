from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

result = set()
for perm in permutations(cards, k):
    number = ''.join(perm)
    result.add(number)

print(len(result))