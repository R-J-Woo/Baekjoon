# 투 포인터 사용

import sys
input = sys.stdin.readline

def search(nums, target_index):
    start, end = 0, len(nums) - 1
    while start < end:
        # 자기 자신이 연산에 포함되는 경우는 건너뜀
        if start == target_index:
            start += 1
            continue
        elif end == target_index:
            end -= 1
            continue

        target = nums[target_index]
        sum = nums[start] + nums[end]
        if sum == target:
            return True
        elif sum > target:
            end -= 1
        else:
            start += 1

    return False

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
for i in range(len(nums)): # O(N)
    # 탐색 결과 좋은 수라면 count를 1 증가
    is_good = search(nums, i) # O(N)
    if is_good:
        count += 1

print(count)