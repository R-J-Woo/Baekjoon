t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())

    result = 0
    while n >= x and n >= y:
        if x < y:
            x += y
        else:
            y += x

        result += 1

    print(result)