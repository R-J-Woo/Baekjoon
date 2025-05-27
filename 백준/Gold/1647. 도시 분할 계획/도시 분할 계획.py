# 아이디어
# 최소 신장 트리에서 가장 비용이 큰 간선 하나를 제거하면 두 개의 마을로 나뉘게 됨

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 유지비 오름차순으로 정렬
edges.sort()

result = 0
max_edge = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않으면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_edge = max(max_edge, cost)

print(result - max_edge)