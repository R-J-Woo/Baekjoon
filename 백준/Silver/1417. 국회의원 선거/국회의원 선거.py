# 아이디어: 기호 1번을 제외한 사람들이 받은 표 중 가장 큰 수를 가져와서 1번과 비교한 후
# 1번의 표보다 크면 1번의 표를 1 늘리고 가장 큰 수의 표를 1줄이는 방식으로 한다
# 기호 1번을 제외한 사람들의 표 중 가장 큰 수가 기호 1번보다 작으면 종료
# 우선순위 큐 이용

import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

if len(nums) == 1:
    print(0)
else:
    first = nums[0]
    other = []
    for i in range(1, len(nums)):
        heapq.heappush(other, -nums[i])

    count = 0
    while True:
        max_value = -heapq.heappop(other)
        if max_value >= first:
            count += 1
            first += 1
            max_value -= 1
            heapq.heappush(other, -max_value)
        else:
            print(count)
            break