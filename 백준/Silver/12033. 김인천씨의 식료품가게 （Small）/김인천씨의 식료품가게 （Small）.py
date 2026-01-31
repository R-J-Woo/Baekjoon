T = int(input())
for case in range(1, T + 1):
    N = int(input())
    P = list(map(int, input().split()))

    result = []
    while True:
        if len(P) == 0:
            break

        price = P[-1]
        sale = (price // 4) * 3
        result.append(sale)

        P.remove(price)
        P.remove(sale)

    result.sort()
    print("Case #" + str(case) + ":", ' '.join(map(str, result)))