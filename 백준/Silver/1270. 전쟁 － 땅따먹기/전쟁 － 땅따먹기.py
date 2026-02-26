N = int(input())

for _ in range(N):
    area = list(map(int, input().split()))
    count, area = area[0], area[1:]

    result = {}
    for a in area:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1

    flag = False
    num = 0
    for key in result:
        # 병사가 절반을 초과
        if result[key] > (count // 2):
            flag = True
            num = key

    if flag:
        print(num)
    else:
        print("SYJKGW")