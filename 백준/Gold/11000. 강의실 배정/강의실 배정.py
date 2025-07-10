# 아이디어: 수업의 시작 시간 기준으로 오름차순 정렬
# 첫 번째로 시작하는 수업의 종료 시간을 우선순위큐에 삽입
# 종료시간이 시작시간보다 늦으면 그 수업의 종료 시간을 우선순위큐에 삽입
# 그 다음 시작 시간이 우선순위큐에 있는 종료시간보다 늦으면 큐에서 삭제하고 그 수업의 종료시간을 삽입
# 마지막까지 반복했을 때 큐에 남아있는 수업 개수가 강의실의 개수

import heapq
import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    s, t = map(int, input().split())
    times.append((s, t))

times.sort()

queue = [times[0][1]]
for i in range(1, n):
    if queue[0] <= times[i][0]: # 종료 시간이 이후 수업 시작 시간보다 빠르다면
        heapq.heappop(queue)
    heapq.heappush(queue, times[i][1])

print(len(queue))