N, M = map(int, input().split())

arr = [0] * 101

# 첫 번째 경기
for i in range(1, N + 1):
    rank = int(input())

    if arr[rank] != 0 and i != 1:
        for j in range(i - 1, rank - 1, -1):
            arr[j + 1] = arr[j]
    arr[rank] = i

ans = [0] * 101

# 두 번째 경기
for i in range(1, M + 1):
    rank = int(input())

    player = arr[M - i + 1]

    if ans[rank] != 0 and i != 1:
        for j in range(i - 1, rank - 1, -1):
            ans[j + 1] = ans[j]
    ans[rank] = player

# 출력
for i in range(1, 4):
    print(ans[i])