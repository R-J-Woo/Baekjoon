# 아이디어: 최소 신장 트리 알고리즘 이용

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 루트 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:  # 종료 조건
        break

    # 부모를 자기 자신으로 초기화
    parent = [i for i in range(m)]

    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z

    # 간선 비용 기준 정렬
    edges.sort()

    mst_cost = 0
    for cost, a, b in edges:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_cost += cost
    
    # 최소 신장 트리를 이용한 비용을 전체에서 빼기
    print(total - mst_cost)
