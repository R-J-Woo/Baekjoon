# 이름의 길이만 중요함 (len(name))
# 인덱스 차이가 K 이내인 학생들만 비교
# 이름 길이별로 슬라이딩 윈도우 / 큐를 두고 관리

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
names = [len(input().strip()) for _ in range(n)]

result = 0
queues = [deque() for _ in range(21)]  # 이름 길이: 1~20까지

for i in range(n):
    length = names[i]
    
    # 슬라이딩 윈도우: 현재 위치에서 k 초과한 학생 제거
    while queues[length] and i - queues[length][0] > k:
        queues[length].popleft()

    # 현재 줄에 있는 친구들 수가 곧 좋은 친구 수
    result += len(queues[length])
    
    # 현재 학생 추가
    queues[length].append(i)

print(result)
