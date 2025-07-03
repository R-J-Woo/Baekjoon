import sys
input = sys.stdin.readline

def binary_search(nums, m):
    start, end = 0, max(nums)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for num in nums:
            if num <= mid:
                total += num
            else:
                total += mid

        if total > m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


n = int(input())
nums = list(map(int, input().split()))
m = int(input())

max_value = binary_search(nums, m)
print(max_value)