i = int(input())

for _ in range(i):
    m = int(input())

    a = m // 25
    m %= 25
    b = m // 10
    m %= 10
    c = m // 5
    m %= 5
    d = m // 1

    print(a, b, c, d)