senario = 0
while True:
    senario += 1
    n = int(input())

    if n == 0:
        break

    names = [input() for _ in range(n)]

    ring = {}
    for _ in range(2 * n - 1):
        number, alpha = input().split()
        if number not in ring:
            ring[number] = alpha
        elif number in ring and ring[number] != alpha:
            ring.pop(number)

    for key in ring:
        print(senario, names[int(key)-1])