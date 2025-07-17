import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = dict()

# O(N): 100,000
for i in range(1, n + 1):
    tempA = list(map(int, input().split()))
    for num in tempA[1:]:
        if num not in A:
            A[num] = []
        heapq.heappush(A[num], i)

# O(B): 200,000
result = [0] * (n + 1)
B = list(map(int, input().split()))
for num in B:
    # 초밥을 원하는 손님이 없거나 큐가 비어있으면 건너뜀
    if num not in A or not A[num]:
        continue

    customer = heapq.heappop(A[num])
    result[customer] += 1

print(' '.join(str(num) for num in result[1:]))