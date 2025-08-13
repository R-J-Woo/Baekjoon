# 아이디어: 큐를 이용
# B를 최대한 많이 지워야 한다
# 거능한 B와 C의 조합은 앞 순서의 B부터 매칭한다 -> FIFO(큐)

from collections import deque
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
removed = [False] * n
answer = 0
que = deque()

# BC 조합 먼저
for i, ch in enumerate(s):
    if ch == 'B':
        que.append(i)
    elif ch == 'C' and que:
        b_idx = que.popleft()
        removed[b_idx] = True
        answer += 1

# AB 조합
a_count = 0
for i, ch in enumerate(s):
    if removed[i]:
        continue
    if ch == 'A':
        a_count += 1
    elif ch == 'B' and a_count:
        a_count -= 1
        answer += 1

print(answer)