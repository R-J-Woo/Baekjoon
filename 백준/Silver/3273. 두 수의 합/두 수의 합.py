import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# 정렬
nums.sort()

count = 0
left = 0
right = n - 1

# 투 포인터 이용
while left < right:
    total = nums[left] + nums[right]

    if total == x:
        count += 1
        left += 1
        right -= 1
    elif total > x:
        right -= 1
    else:
        left += 1

print(count)