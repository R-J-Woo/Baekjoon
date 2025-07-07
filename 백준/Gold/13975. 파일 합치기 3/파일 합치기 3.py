# 아이디어: 파일 크기가 가장 작은 두개를 골라서 합친다
# 그 후 다시 리스트에 넣는다
# 파일이 합쳐져서 1개가 남을 때까지 반복한다

import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    k_list = list(map(int, input().split()))
    heapq.heapify(k_list)

    count = 0
    while True:
        if len(k_list) <= 1:
            break

        c1 = heapq.heappop(k_list)
        c2 = heapq.heappop(k_list)
        x = c1 + c2
        count += x
        heapq.heappush(k_list, x)

    print(count)