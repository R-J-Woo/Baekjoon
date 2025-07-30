# 아이디어: 우선순위 큐 사용
# 일반 리스트로 하면 시간 초과 발생 -> 우선순위 큐 사용하여 시간 초과 방지

import heapq
import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    number, start, end = map(int, input().split())
    times.append((start, end))

times.sort() # 시작 시간과 종료 시간 순서대로 정렬
room = []
heapq.heappush(room, times[0][1])  # 첫 강의의 종료 시간 저장
for i in range(1, n): # O(N)
    # 가장 빨리 끝나는 강의실이 비어있다면 재사용
    if room[0] <= times[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, times[i][1])

print(len(room))