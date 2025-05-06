import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 1. 산술평균
mean = round(sum(nums) / n)

# 2. 중앙값
nums_sorted = sorted(nums)
median = nums_sorted[n // 2]

# 3. 최빈값
count = Counter(nums)
mode_list = count.most_common()

# 최빈값 여러 개일 경우 처리
max_freq = mode_list[0][1]
modes = [k for k, v in mode_list if v == max_freq]

if len(modes) > 1:
    mode = sorted(modes)[1]  # 두 번째로 작은 값
else:
    mode = modes[0]

# 4. 범위
range_ = max(nums) - min(nums)

# 출력
print(mean)
print(median)
print(mode)
print(range_)
