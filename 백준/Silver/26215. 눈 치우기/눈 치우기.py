# 그리디 알고리즘: 눈이 많이 쌓인 집부터 치움
# 우선순위 큐 사용하여 눈이 많이 쌓인 집을 선택 후 치우기

import heapq

N = int(input())
a = list(map(int, input().split()))

A = []
for num in a:
    heapq.heappush(A, -num)

result = 0
while A:
    if len(A) >= 2:
        num1 = -heapq.heappop(A)
        num2 = -heapq.heappop(A)

        num1 -= 1
        num2 -= 1

        if num1 > 0:
            heapq.heappush(A, -num1)
        
        if num2 > 0:
            heapq.heappush(A, -num2)

    else:
        num1 = -heapq.heappop(A)
        num1 -= 1
        if num1 > 0:
            heapq.heappush(A, -num1)

    result += 1
        

if result > 1440:
    print(-1)
else:
    print(result)