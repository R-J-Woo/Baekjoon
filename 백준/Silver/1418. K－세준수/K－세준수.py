N = int(input())
K = int(input())

result = 0

for num in range(1, N + 1):
    value = num
    max_value = 1
    i = 2

    while i * i <= value:
        if value % i == 0:
            max_value = max(max_value, i)
            while value % i == 0:
                value //= i
        i += 1

    if value > 1:  # 남은 소수
        max_value = max(max_value, value)

    if max_value <= K:
        result += 1

print(result)