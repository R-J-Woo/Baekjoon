while True:
    N = int(input())
    if N == 0:
        exit()

    result = []
    max_height = '0'
    for _ in range(N):
        name, height = input().split()
        if height > max_height:
            result.clear()
            result.append(name)
            max_height = height
        elif height == max_height:
            result.append(name)

    print(' '.join(result))