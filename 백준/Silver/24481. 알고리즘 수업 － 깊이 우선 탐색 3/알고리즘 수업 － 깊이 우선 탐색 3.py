import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호 오름차순 정렬
for g in graph:
    g.sort()

depth = [-1] * (n + 1)
stack = [(r, 0)]  # (노드 번호, depth)

while stack:
    node, d = stack.pop()
    if depth[node] != -1:
        continue
    depth[node] = d
    for neighbor in reversed(graph[node]):  # stack은 LIFO → 뒤에서부터 넣기
        if depth[neighbor] == -1:
            stack.append((neighbor, d + 1))

for i in range(1, n + 1):
    print(depth[i])
