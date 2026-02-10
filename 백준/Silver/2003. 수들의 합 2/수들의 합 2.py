n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
current_sum = 0
count = 0

while True:
    if current_sum >= m:
        current_sum -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += nums[end]
        end += 1

    if current_sum == m:
        count += 1

print(count)
