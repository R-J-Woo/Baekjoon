# 플로이드-워셜 알고리즘 사용
# 아이디어: 알파벳을 숫자로 변환한 후 그래프 생성
# ex) a -> 1, b -> 2 ...

import sys
input = sys.stdin.readline

n = int(input())
graph = [[float('INF')] * 27 for _ in range(27)] # 알파벳 수만큼 그래프 행렬 생성
for i in range(1, 27):
    graph[i][i] = 0

for _ in range(n):
    words = input().strip()
    x, y = words[0], words[-1]
    x = ord(x) - 96
    y = ord(y) - 96
    graph[x][y] = 0

# 플로이드 워셜 실행
for k in range(1, 27):
    for i in range(1, 27):
        for j in range(1, 27):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

m = int(input())
for _ in range(m):
    words = input().strip()
    x, y = words[0], words[-1]
    x = ord(x) - 96
    y = ord(y) - 96
    if graph[x][y] == 0:
        print('T')
    else:
        print('F')