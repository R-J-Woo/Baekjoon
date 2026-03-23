N = int(input())

result = set()
for num1 in range(N + 1):
    for num2 in range(N + 1):
        for num3 in range(N + 1):
            for num4 in range(N + 1):
                if num1 + num2 + num3 + num4 == N:
                    total = num1 + 5 * num2 + 10 * num3 + 50 * num4
                    result.add(total)

print(len(result))