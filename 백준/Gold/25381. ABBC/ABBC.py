# 아이디어: B&C를 먼저 시행하고, 그 후 A&B를 시행한다

from collections import deque

s = input()
queue = deque()
c_count = 0
result = 0
# BC를 먼저 시행 -> 역으로 순회하면서 큐에 삽입
for i in range(len(s) - 1, -1, -1):
    alpha = s[i]
    if alpha == 'C':
        c_count += 1
    # B 뒤에 C가 있다면 삭제 -> 큐에 넣지 않음
    elif alpha == 'B' and c_count > 0:
        c_count -= 1
        result += 1
    else:
        queue.appendleft(alpha)
        
# AB를 그 후 시행
length = len(queue)
a_count = 0
for _ in range(length):
    alpha = queue.popleft()
    if alpha == 'A':
        a_count += 1
    # B 전에 A가 나온 적이 있다면 삭제
    elif alpha == 'B' and a_count > 0:
        a_count -= 1
        result += 1

print(result)