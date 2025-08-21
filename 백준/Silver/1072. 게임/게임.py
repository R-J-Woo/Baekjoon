# 아이디어: 이분탐색으로 적절한 횟수를 탐색

x, y = map(int, input().split())
z = (y * 100) // x

start = 0
end = 1000000000
result = -1
while start <= end:
    mid = (start + end) // 2
    temp_x, temp_y = x + mid, y + mid
    if z < (temp_y * 100) // temp_x:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)