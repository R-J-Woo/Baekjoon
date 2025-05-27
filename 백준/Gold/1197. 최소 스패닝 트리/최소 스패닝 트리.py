import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # recursion error 발생 -> 재귀 깊이 제한 증가

# 특정 원소의 루트 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = []
result = 0
for _ in range(e):
    a, b, c = map(int, input().strip().split())
    edges.append((c, a, b))

# 간선을 비용 오름차순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
