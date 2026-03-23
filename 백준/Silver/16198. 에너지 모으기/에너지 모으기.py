def dfs(arr, energy):
    global result

    # 종료 조건
    if len(arr) == 2:
        result = max(result, energy)
        return

    # 중간 원소 하나씩 제거
    for i in range(1, len(arr) - 1):
        gain = arr[i-1] * arr[i+1]
        new_arr = arr[:i] + arr[i+1:]

        dfs(new_arr, energy + gain)


N = int(input())
W = list(map(int, input().split()))

result = 0
dfs(W, 0)

print(result)