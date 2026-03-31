from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

result = 0
for numbers in permutations(A):
    total = 0
    for i in range(len(numbers) - 1):
        total += abs(numbers[i] - numbers[i+1])

    result = max(result, total)

print(result)