# 아이디어: 큐 (deque)를 사용한다
# 순서대로 진행해나가면서 K의 배수거 아닌 경우에는 popleft 후 다시 append 해서 넣어주고 K의 배수 번째 인 경우는 삭제

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
string = []

# 큐 초기화
for i in range(1, n + 1):
    queue.append(i)

index = 0
while queue:
    index += 1
    if index % k != 0:
        num = queue.popleft()
        queue.append(num)
    else:
        num = queue.popleft()
        string.append(num)

print('<' + ', '.join(map(str, string)) + '>')
