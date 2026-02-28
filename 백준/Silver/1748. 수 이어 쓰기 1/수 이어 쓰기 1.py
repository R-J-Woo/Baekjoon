N = int(input())
length = len(str(N))

result = 0

for i in range(1, length):
    result += 9 * (10 ** (i - 1)) * i

result += (N - 10 ** (length - 1) + 1) * length

print(result)